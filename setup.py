#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name = "utrace",
    version = "1.1.0",
    url = 'https://github.com/ondrejsika/python-utrace',
    license = 'MIT',
    description = 'Python wrapper for utrace.de XML API.',
    author = 'Ondrej Sika',
    author_email = 'ondrej@ondrejsika.com',
    py_modules = ['utrace'],
    install_requires = ['requests'],
)
