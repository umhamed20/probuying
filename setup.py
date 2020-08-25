# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in probuying/__init__.py
from probuying import __version__ as version

setup(
	name='probuying',
	version=version,
	description='Buying purpose',
	author='Aisha',
	author_email='aisha@gmail.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
