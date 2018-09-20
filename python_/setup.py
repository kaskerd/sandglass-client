import sys

from os import path
from codecs import open
from setuptools import setup, find_packages

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='sandglass',

    version=1,

    description='Sandglass python client',

    long_description=long_description,

    url='https://github.com/sandglass/python',

    author='Sandglass',

    author_email='info@sandglass.stream',

    license='MIT',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',

        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',

        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],

    keywords='sandglass, message queue, task queue',

    packages=find_packages(exclude=['contrib', 'docs', 'tests']),

    install_requires=[
      "googleapis-common-protos>=1.5.3",
      "grpcio>=1.15.0",
      "grpcio-tools>=1.15.0"
    ]
)