#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  6 16:05:14 2017

PDF Scraper: Grabs a [list of] links from a .csv file &
             downloads a PDF from each link & saves it to
             a user-defined local path

@author: alex laz
"""

from selenium import webdriver
import requests
import time
import csv

def init():
    '''
    Display welcome message & ask user to input the path
    with the location of the CSV file

    return: int, selection #
    '''

    # Welcome message
    print('------------------')
    print('PDF Scraper V1.0.0')
    print('------------------')

    # Determine which type of operation the user requries
    print('Type of scrape to perform (input #): ')
    print('     1) CSV list: Protected PDFs (app.box.com)')
    print('     2) CSV list: Unprotected PDFs')
    print('     3) Single unprotected PDF')

    # Check the users input for a valid selection
    while True:
        selection = input('> ')
        if selection == str(1) or selection == str(2) or selection == str(3):
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


def getPath():
    '''
    Ask user to input the path
    with the location of the CSV file

    return: filepath with location of CSV
    '''
    # Check the users input for a working path
    while True:
        print("Enter the path where your CSV is located")
        print("(Type 'h' for help)")
        filepath = input('Path: ')
        if filepath == 'h':
            print('')
            print('Example: /Users/joe/Desktop/list_of_urls.csv')
            print('')
            continue
        else:
            try:
                fh = open(filepath, 'r')
                break
            except IOError:
                print('Cannot open ', filepath)
                continue
            else:
                # Close the file after correct input
                fh.close()

    return filepath

def importLinks(filepath, columnNum):
    '''
    filepath: str, the filepath for the .csv containing the links
    columnNum: int, the column # containing the URLs

    return: list of URLs from the csv file
    '''
    links = []
    with open(filepath, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            if 'http' in row[(columnNum - 1)]:
                links.append(row[(columnNum - 1)])
            else:
                links.append('http://' + row[(columnNum - 1)])

    return links

def downloadProtectedPDFs(linkList, downloadPath):
    '''
    linkList: a list of links
    downloadPath: str, location where PDFs will be output
    '''

    # Launches automated verison of chrome
    chrome_options = webdriver.ChromeOptions()
    prefs = {'download.default_directory' : downloadPath}
    chrome_options.add_experimental_option('prefs', prefs)
    # This line won't work on other machines - need to adjust this
    browser = webdriver.Chrome('/Users/alex/Desktop/pdf_scraper/chromedriver',chrome_options=chrome_options)
    for i in range(len(linkList)):
        browser.get(linkList[i])

        try:
            elem = browser.find_element_by_tag_name('button')
        except:
            print('Was not able to find an element with that name.')

        elem.click()
        # Waits 2 seconds inbetween requests to avoid getting IP ban
        time.sleep(2)
    # Wait 5 seconds for last PDF to download before closing browser
    time.sleep(5)

    browser.close()

def downloadUnprotectedPDFs(linkList, downloadPath):
    '''
    linkList: a list of links
    downloadPath: str, location where PDFs will be output
    '''
    for i in range(len(linkList)):
        # Establish connection to the site
        url = linkList[i]
        r = requests.get(url)

        # Grab the filename from URL string
        filename = url.split('/', -1)
        filename = filename[-1]
        filepath = downloadPath + '/' + filename
        print(filepath)

        # Download the pdf
        with open(filepath,'wb') as f:
            f.write(r.content)

def singleURLScrape():
    '''
    Grabs the PDF & outputs it
    '''
    filepath = input('Enter the path where the PDF will be saved: ')
    url = input('Enter the URL: ')

    # Establish connection to the site
    r = requests.get(url)

    # Download the pdf
    filename = url.split('/', -1)
    filename = filename[-1]
    filepath = filepath + '/' + filename
    with open(filepath,'wb') as f:
        f.write(r.content)
        f.close()

def run():
    #===================Program Start====================================#
    selection = init()

    if selection == 1 or selection == 2:
        filepath = getPath()

        # Grab list of links
        columnNum = int(input('Enter the column # that contains the URLs: '))
        links = importLinks(filepath, columnNum)

        # Prompt user to set the download path
        downloadPath = input('Enter the path where the PDFs will be output: ')

        # Download PDFs
        if selection == 1:
            # Protected PDFs - uses Selenium & Webdriver
            downloadProtectedPDFs(links, downloadPath)
        else:
            # Unprotected PDFs - uses 'requests' module
            downloadUnprotectedPDFs(links, downloadPath)

    # End Program
    print('Done!')
    #====================================================================#
    
    
run()
