#!/usr/bin/env python

from setuptools import setup, find_packages

version = __import__('fakename').__version__
setup(
    name='py-fakename',
    version=version,
    author='Mark Ignacio',
    author_email='mark@ignacio.io',
    description='Wrapper for fakena.me generation',
    url='https://github.com/mark-ignacio/py-fakename',
    license='GPL',
    packages=find_packages(),
    install_requires=['requests'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Topic :: Internet',
    ]
)
