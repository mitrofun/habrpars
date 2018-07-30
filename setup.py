import os
import sys

from setuptools import setup, find_packages
from os.path import join, dirname

sys.path.insert(0, os.path.join(os.path.abspath('.'), 'habrpars'))

CURRENT_PYTHON = sys.version_info[:2]
REQUIRED_PYTHON = (3, 6)

# This check and everything above must remain compatible with Python 2.7.
if CURRENT_PYTHON < REQUIRED_PYTHON:
    sys.stderr.write("""
==========================
Unsupported Python version
==========================
This version of topverbs requires Python {}.{}
""")

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='habrpars',
    entry_points={'console_scripts': [
        'habrpars = habrpars.habrpars:main',
    ]},
    version='0.1',
    install_requires=[
        'bs4>=0.0.1',
        'beautifulsoup4>=4.6.0',
        'requests>=2.19.1',
        'pymorphy2>=0.8',
        'pymorphy2-dicts-ru>=2.4.404381.4453942'
    ],
    packages=find_packages(),
    long_description=open(join(dirname(__file__), 'README.md')).read(),
    url='https://github.com/mitrofun/habrpars',
    description='Analyzer of the frequency of use of nouns in the headings of posts on habr.com',
    classifiers=[
        'Development Status :: 1 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
        'Topic :: Text Processing :: Analytics',
    ],
    keywords='noun parse habr',
    author='Dmitry Shesterkin',
    author_email='mitri4@bk.ru',
    license='MIT',
    setup_requires=['pytest-runner'],
    tests_require=[
        'pytest',
        'pytest-flake8',
        'flake8',
        'requests-mock',
        'bs4>=0.0.1',
        'beautifulsoup4>=4.6.0',
        'requests>=2.19.1',
        'pymorphy2>=0.8',
        'pymorphy2-dicts-ru>=2.4.404381.4453942'
    ],
    test_suite='tests',
    zip_safe=False
)
