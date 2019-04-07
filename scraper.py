# Simple Web Scraper using Python
# by <Enter your name here>

import re
import time
import csv
from selenium import webdriver
from bs4 import BeautifulSoup

def getHTML(driver, baseURL, path):
    '''This function takes the selenium webdriver, the base URL and the path where the HTML is located. It generates and returns the HTML using 
        the driver'''
    # TODO(): Get the document from the driver using the get() method. The get() method takes the URL of the document.

    # TODO(): Implement a time delay using the sleep function in the time module. This function takes a parameter of time in seconds.

    # TODO(): Render the HTML from the document and return it.
    return 

def initializeCSV(fileName, fieldNames):
    '''This function creates a CSV writer object from the filename provided, writes the field names for the csv file, and returns a writer object'''
    # TODO(): Open the CSV file using the filename parameter.
    
    # TODO(): Creater a dictionary writer object from the csv package.
    writer = 
    
    # TODO(): Write the header of the CSV file.

    # TODO(): Return the writer object.
    return 

def getQualifications(job):
    '''For each job, gets the list of qualifications from the soup obj'''
    qualsList = []

    # TODO(): Loop through all the qualifications using their respective class identifier.
    for _ in _:
        pass

    # TODO(): Return the qualifications generated.
    return 

def getPrompt(job):
    '''For each job, gets the deliverable prompt from the soup object'''
    promptsList = []

    # TODO(): Loop through all the prompts using their respective class identifier.
    for _ in _:
        pass

    # TODO(): Return the list of prompts generated.    
    return 


if __name__ == '__main__':

    baseURL = 'https://www.hackuci.com'

    # FOR WINDOWS USERS: Add a '.exe' to the path specified below.
    driver = webdriver.Chrome('./webdrivers/chromedriver')

    # TODO(): Get the recruit page html.
    recruitHTML = 
    
    # TODO(): Create a BeautifulSoup object using the HTML generated above.
    soup = 

    # TODO(): Create a regular expression that matches the different positions on the recruitment website.
    positionsRE = 

    # TODO(): Extract the HTML of the navigation bar of the recruitment website.
    navbarMenu = 

    # TODO(): Filter all the links in the navbarMenu HTML and get the ones that match the regular expression created above.
    relativePaths = 

    # TODO(): Print out the relative paths generated above.
    for _ in _:
        pass

    # This is the list of fields of information we are going to extract from the job listings.
    fieldnames = ["role", "description", "qualifications","prompt"]

    # TODO(): Write the information to a CSV file.
    writer = 

    data = {"role":"", 
            "description": "",
            "qualifications": "", 
            "prompt": ""}

    # TODO(): Get the technology webpage from the recruitment site.
    positionsHTML = 

    # TODO(): Create a soup for the position HTMl generated above.
    soup = 

    # TODO(): Iterate through 
    for job in _:

        # TODO(): Write the data for each key in the data dictionary.

        data["role"] = 
        data["description"] = 
        
        data["qualifications"] = 
        data["prompt"] = 

        # TODO(): Write the data into the CSV file using the writer object. Each instance of the data is a row in the CSV file. 
        

    driver.quit()





