from setuptools import setuptools, find_packages

setup(name='{{cookiecutter.package_name}}',
      version='0.1.0',
      author={{cookiecutter.author_name}}
      packages=find_packages()
      )

