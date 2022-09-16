# -*- coding: utf-8 -*-

# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path

from korean_lunar_calendar import __version__

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='korean_lunar_calendar',
    version=__version__,
    description='Korean Lunar Calendar',
    long_description=long_description,
    packages=find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
    url='https://github.com/usingsky/korean_lunar_calendar_py',
    author='Jinil Lee',
    author_email='usingsky@gmail.com',
    maintainer='Jinil Lee',
    maintainer_email='usingsky@gmail.com',
    keywords=['calendar', 'korean', 'lunar'],
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: End Users/Desktop',
        'Topic :: Software Development :: Libraries',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
    ]
)
