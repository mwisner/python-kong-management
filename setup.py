#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'requests',
]

setup_requirements = [
    'pytest-runner',
]

test_requirements = [
    'pytest',
    'requests',
]

setup(
    name='python_kong_management',
    version='0.2.2',
    description="Python api wrapper for Kong API Gatway",
    long_description=readme + '\n\n' + history,
    author="Matt Wisner",
    author_email='mwisner@fourthlab.com',
    url='https://github.com/mwisner/python-kong-management',
    packages=find_packages(include=['kong']),
    include_package_data=True,
    install_requires=requirements,
    license="MIT license",
    zip_safe=False,
    keywords='python-kong-management',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    test_suite='tests',
    tests_require=test_requirements,
    setup_requires=setup_requirements,
)
