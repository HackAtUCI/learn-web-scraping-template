# Simple Web Scraper using Python
# by <Enter your name here>

import re
import time
import csv
from selenium import webdriver
from bs4 import BeautifulSoup

def get_html(driver, base_url, path):
    '''This function takes the selenium webdriver, the base URL and the path where the HTML is located. It generates and returns the HTML using 
        the driver'''
    # TODO(2): Get the document from the driver using the get() method. The get() method takes the URL of the document.
    driver.get(base_url+path)
    # TODO(3): Implement a time delay using the sleep function in the time module. This function takes a parameter of time in seconds.
    time.sleep(1)
    # TODO(4): Render the HTML from the document and return it.
    return driver.execute_script("return document.documentElement.outerHTML")

def initialize_csv(file_name, fieldnames):
    '''This function creates a CSV writer object from the filename provided, writes the field names for the csv file, and returns a writer object'''
    # TODO(10): Open the CSV file using the filename parameter.
    file = open(file_name, "w")
    # TODO(11): Creater a dictionary writer object from the csv package.
    writer = csv.DictWriter(file, fieldnames)
    
    # TODO(12): Write the header of the CSV file.
    writer.writeheader()

    return writer

def get_qualifications(job):
    '''For each job, gets the list of qualifications from the soup obj'''
    quals_list = []

    # TODO(18): Loop through all the qualifications using their respective class identifier.
    for item in job.find_all("div", class_ = "item"):
        quals_list.append(item.text.strip('\n'))

    return quals_list 

def get_prompt(job):
    '''For each job, gets the deliverable prompt from the soup object'''
    prompts_list = []

    # TODO(19): Loop through all the prompts using their respective class identifier.
    for prompt in job.find_all("a"):
        prompts_list.append(prompt["href"])

    return prompts_list 


if __name__ == '__main__':

    base_url = 'https://www.hackuci.com'

    # FOR WINDOWS USERS: Add a '.exe' to the path specified below.
    driver = webdriver.Chrome('./webdrivers/chromedriver.exe')

    # TODO(1): Get the recruit page html.
    recruit_html = get_html(driver, base_url, "/recruit")
    
    # TODO(5): Create a BeautifulSoup object using the HTML generated above.
    soup = BeautifulSoup(recruit_html, "html.parser")

    # TODO(6): Extract the HTML of the navigation bar of the recruitment website.
    navbar_menu = soup.find("div", class_ = "navbar-menu")

    # TODO(7): Create a regular expression that matches the different positions on the recruitment website.
    positions_re = re.compile("/recruit/[a-z]+")

    # TODO(8): Filter all the links in the navbarMenu HTML and get the ones that match the regular expression created above.
    relative_paths = navbar_menu.find_all(lambda tag: tag.has_attr("href") and positions_re.match(tag["href"]))

    # TODO(9): Print out the relative paths generated above.
    for a_tag in relative_paths:
        print(a_tag["href"])

    # This is the list of fields of information we are going to extract from the job listings.
    fieldnames = ["ROLE", "DESCRIPTION", "QUALIFICATIONS","PROMPT"]

    # TODO(13): Write the information to a CSV file.
    writer = initialize_csv("role.csv", fieldnames)

    data = {"ROLE":"", 
            "DESCRIPTION": "",
            "QUALIFICATIONS": "", 
            "PROMPT": ""}

    # TODO(14): Get the technology webpage from the recruitment site.
    positions_html = get_html(driver, base_url, "/recruit/technology")

    # TODO(15): Create a soup for the position HTML generated above.
    soup = BeautifulSoup(positions_html, "html.parser")

    # TODO(16): Iterate through 
    for job in soup.find_all("div", class_ = "job"):

        # TODO(17): Write the data for each key in the data dictionary.

        data["ROLE"] = job.find("div", class_ = "job-title").text.strip('\n')
        data["DESCRIPTION"] = job.find("span").text.strip('\n')
        
        data["QUALIFICATIONS"] = get_qualifications(job)
        data["PROMPT"] = get_prompt(job)

        # TODO(20): Write the data into the CSV file using the writer object. Each instance of the data is a row in the CSV file. 
        writer.writerow(data)

    driver.quit()





