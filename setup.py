# coding=utf-8
'''ml-trainer: a deep learning toolbox for google cloud ml engine.
'''

from setuptools import setup, find_packages
from codecs import open
from os import path

from setuptools import setup, find_packages
here = path.abspath(path.dirname(__file__))

REQUIRED_PACKAGES = ['numpy>=1.15',
                     'pandas>=0.19',
                     'tensorflow==1.13.1']


# Get the long description from the README.md file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

# Get the long description from the LICENSE file
with open(path.join(here, 'LICENSE'), encoding='utf-8') as f:
    license = f.read()


setup(
    name='trainer',
    version='0.1.0',
    keywords='deep learning deep_learning machine machine_learning natural language processing computer vision',
    author="Aashish Dahiya",
    long_description_content_type='text/markdown',
    author_email="aashish.dahiya1008@gmail.com",
    install_requires=REQUIRED_PACKAGES,
    url="https://skyl.ai",
    include_package_data=True,
    description='Keras trainer',
    long_description=long_description,
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)

