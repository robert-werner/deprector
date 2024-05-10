from setuptools import setup, find_packages

with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
    name='deprector',
    version='0.1',
    description='Russian depression detector',
    author='Leonid Kolesnichenko',
    author_email='xperience439@gmail.com',
    packages=['deprector'],
    install_requires=required
)