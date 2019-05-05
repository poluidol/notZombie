#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

ROOT_PACKAGE_NAME = 'not_zombie'


def parse_requirements():
    with open('requirements.txt') as f:
        return f.read().splitlines()


setup(
    name=ROOT_PACKAGE_NAME,
    version='1.0',
    author=['poluidol'],
    packages=find_packages(),
    long_description='not_zombies',
    requirements=parse_requirements()
)
