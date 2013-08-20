#!/usr/bin/env python
"""Pythonic Setup for Git Flow (AVH Edition)."""


import setuptools

import gflib


setuptools.setup(
    version='1.1.0',
    name='pygitflow-avh',
    description='Pythonic Installer for Git Flow (AVH Edition).',
    author='Rajiv Battula',
    author_email='rbattula@splunk.com',
    license='Apache License 2.0',
    url='https://github.com/rajivbattula/pygitflow-avh',
    scripts=gflib.get_gitflow(),
    setup_requires=['nose'],
    tests_require=['nose', 'coverage', 'nose-cov'],
)
