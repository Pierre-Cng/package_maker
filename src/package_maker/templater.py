import os
from string import Template
from package_maker import resources
import argparse
import inspect

def parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('package_name', help='Name of your new python package', nargs="?", default='mypackage')
    parser.add_argument('description', help='Description of the package purpose', nargs="?", default='')
    parser.add_argument('git_url', help='Url of the github repo', nargs="?", default='')
    return parser.parse_args()

class templater:
    root = os.getcwd()

    def create_directory(self, path, name):
        new_dir = os.path.join(path, name)
        os.makedirs(new_dir)
        return new_dir

    def create_init(self, path):
        new_file = os.path.join(path, '__init__.py')
        file = open(new_file, 'w')
        file.close()

    def package_structure(self, package_name):
        src_dir = self.create_directory(self.root, 'src')
        package_dir = self.create_directory(src_dir, package_name)
        self.create_init(package_dir)
        tests_dir = self.create_directory(self.root, 'tests')
        self.create_init(tests_dir)

    def pyproject_toml_file(self, package_name, description, git_url):
        parameters = {"name": f'"{package_name}"', "description": f'"{description}"', "url": f'"{git_url}"'}
        template = open(os.path.join(os.path.dirname(inspect.getfile(resources)), 'pyproject_toml_template.txt'), 'r')
        updated_content = Template(template.read()).safe_substitute(parameters)
        new_toml_file = open(os.path.join(self.root, 'pyproject.toml'), 'w')
        new_toml_file.write(updated_content)
        new_toml_file.close()

def main():
    args=parser()
    template = templater()
    template.package_structure(args.package_name)
    template.pyproject_toml_file(args.package_name, args.description, args.git_url)

if __name__ == '__main__':
    main()
