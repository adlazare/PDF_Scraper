#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  8 13:19:07 2017

@author: alex
"""

'''

Entry Point

'''
'''
__requires__ = 'pdf_scraper==1.0.0'
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.exit(
        load_entry_point('pdf_scraper==1.0.0', 'console_scripts', 'pdf_scraper')()
    )

'''
from .scraper import run

# Initialize program
def main():
    run()
