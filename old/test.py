#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  8 00:41:03 2017

@author: alex
"""
import requests
import csv


def init():
    '''
    Display welcome message & ask user to input the path
    with the location of the CSV file
    
    return: filepath with location of CSV
    '''
    
    # Welcome message
    print('PDF Scraper V1.0.0')
    print('----------------')
    
    # Determine which type of operation the user requries
    print('Type of scrape to perform (input #): ')
    print('     1) CSV list of Protected PDFs (app.box.com)')
    print('     2) CSV list of unprotected PDFs')
    print('     3) Single Protected PDF')
    print('     4) Single Unprotected PDF')
    
    # Check the users input for a working path
    while True:
        # Note: Python 2.x users should use raw_input, the equivalent of 3.x's input
        selection = input('> ')
        if selection == str(1) or selection == str(2) or selection == str(3) or selection == str(4):
            print('Success!')
            selection = int(selection)
            break
        else:
            print('Please select a valid option.')
            continue
    
    # If using a list, run the normal flow of the program
    if selection == 1 or selection == 2:
        return selection
    # If scraping a single URL, run function for manual input
    else:
        singleURLScrape()


def singleURLScrape():
    '''
    return: 
    '''
    filepath = input('Enter the path where the PDF will be saved: ')
    url = input('Enter the URL: ')
    
    # Establish connection to the site
    r = requests.get(url)
    
    # Download the pdf
    filename = url.split('/', -1)
    filename = filename[-1]
    filepath = filepath + '/' + filename
    print(filepath)
    with open(filepath,'wb') as f:
        f.write(r.content)
    
selection = init()
print(selection)
'''
links = []

with open('pdf_test.txt', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        links.append(row[0])
    
for i in range(len(links)):
    # Establish connection to the site
    url = links[i]
    r = requests.get(url)
    
    # Download the pdf
    filename = 'test' + str(i) + '.pdf'
    with open(filename,'wb') as f:
        f.write(r.content)
'''

'''
url = "http://www.axmag.com/download/pdfurl-guide.pdf"
r = requests.get(url) # create HTTP response object
 
with open("test.pdf",'wb') as f:
    f.write(r.content)
'''
    
