# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

REQUIRED_PACKAGES = ['Keras==2.0.4',
                     'h5py==2.7.0']


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='trainer',
    version='0.1.0',
    author="Aashish Dahiya",
    author_email="aashish.d@people10.com",
    install_requires=REQUIRED_PACKAGES,
    url="https://skyl.ai",
    include_package_data=True,
    description='Keras trainer',
    long_description=readme,
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)

