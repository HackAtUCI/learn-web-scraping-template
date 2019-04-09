# Web Scraping Workshop
In this workshop, you will learn how to scrape a dynamic web page (https://www.hackuci.com/recruit) using selenium and BeautifulSoup.

## Setup

### Step 0: Pre-check
Go to your terminal and run these commands in this order:
- python --version
- pip --version

If your system tells you do not have both, download what you don't have. 

### Step 1: Set up a virtual environment 
We set up a virtual environment to avoid code ambiguities in our 
global python library (i.e. two functions with the same name in different modules). 
If these ambiguities occur, they will cause errors and your code will not run.

- pip install virtualenv (you can run "pip list" to see if you already have virtualenv )
- set aside a folder/workspace and cd into it
- run command "virtualenv <environment_name>"

### Step 2: Installing python packages
- for Windows, run "./<environment_name>/scripts/activate".
- for Mac/Linux, run "source ./<environment_name>/bin/activate"
- Then, "pip install -r requirements.txt". <requirements.txt> should already be in the repository.
- You have successfully created your virtual environment and are ready to begin scraping.


## Selenium 
We use selenium to make our script act as a client making requests to a website. This is important when scraping a javascript rendered web page as we need our script to wait for the website's javascript to execute and grab the resulting html. That will have the data we want, not the page source.

To make our script act like a client:

    from selenium import webdriver
    driver = webdriver.Chrome('./webdrivers/chromedriver.exe')
    #chromedrivers are in the repository 
    #chromedriver instead of chromedriver.exe if on Mac/Linux

This will initialize a chrome webdriver and open up a chrome window. 

    driver.get('www.hackuci.com/recruit')
This will open up the page at www.hackuci.com/recruit.

    time.sleep(1)
    html = driver.execute_script('return document.documentElement.outerHTML')
We want to give the page time to execute its javascript. If we grabbed the html too quickly, we would grab the page source, which would be only javascript code.  

This is how we will grab the html from a dynamic website.  

## Beautiful Soup 
We use BeautifulSoup4(bs4) to parse the html we get from selenium and make queries about it. You can think of this soup as a collection of tags, with each tag being a mapping/dictionary of html attributes to their values. 

To create a Beautiful Soup object:

    BeautifulSoup(html, "html.parser")
    # html.parser is the default parser downloaded with your core Python libraries

Some common operations to query the soup are:
- find(tag_name)
    - Returns the first tag with the specified tag name. Can put further arguments for more specific tag such as id = "id name" or class_ = "class name"

- find_all(...)
    - Returns all tags that fit specifications. Arguments can be a tag name, a function, and/or the ways described above in find().

- tag.attrs
    - Returns a dict of all attributes and their values

For more information, refer to the official documentation link below.

## References
- BeautifulSoup4 Docs: https://www.crummy.com/software/BeautifulSoup/bs4/doc/#soupstrainer
- Selenium Docs: https://www.seleniumhq.org/docs/#
- Medium Tutorial: https://medium.freecodecamp.org/better-web-scraping-in-python-with-selenium-beautiful-soup-and-pandas-d6390592e251
- Slides: https://docs.google.com/presentation/d/1y_NsIcOMNCjByvnDMi9gK-_Jvlxj1AO3BnCIi55vCFA/edit#slide=id.gc6f90357f_0_0