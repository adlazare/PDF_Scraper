"""A setuptools based setup module.
See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
"""

# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='pdf_scraper',
    version='1.0',
    packages=['pdf_scraper',],
    description='Grabs PDFs from the web',
    long_description=long_description,
    author='Alex Laz',
    author_email='adlazare@gmail.com',
    license='MIT',
    keywords='scraping pdf download',
    install_requires=['selenium', 'requests'],
    #scripts=['scripts/scraper.py'],
)
