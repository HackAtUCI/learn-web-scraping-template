# Web Scraping Workshop
In this workshop, you will learn how to scrape a dynamic web page (https://www.hackuci.com/recruit) using Selenium and BeautifulSoup.

## Step 1: Pre-requisite Downloads
- Make sure that you have Python3 installed. If you do not, [here is an installation guide](https://realpython.com/installing-python/).
- Make sure you have the latest version of Google Chrome (Version 87)

## Step 1: Download the project
Clone the repo using:
```
git clone https://github.com/hackuci/learn-web-scraping-template.git
```
Navigate into the project directory:
```
cd learn-web-scraping-template
```

## Step 2: Set up a virtual environment 
We set up and activate a virtual environment to avoid code ambiguities in our 
global python library.

On macOS and Linux:
```
python3 -m venv env
source env/bin/activate
```
On Windows:
```
py -m venv env
.\env\Scripts\activate.bat
```

## Step 3: Installing Python dependencies
We install the dependencies that this project requires into the virtual environment using:
```
python -m pip install -r requirements.txt
```

## Step 4: Run the project
Run the project using:
```
python scraper.py
```

**If you see the following error message, please update your Google Chrome to version 87:**
```
This version of ChromeDriver only supports Chrome version 87
Current browser version is 86.0.4240.198
```

---

## Selenium 
We use selenium to make our script act as a client making requests to a website. This is important when scraping a javascript rendered web page as we need our script to wait for the website's javascript to execute and grab the resulting html. That will have the data we want, not the page source.

This will initialize a chrome webdriver and open up a chrome window. 
```
driver.get('www.hackuci.com/recruit')
```
This will open up the page at www.hackuci.com/recruit.
```
time.sleep(2)
html = driver.find_element_by_tag_name('html').get_attribute('innerHTML')
```
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
- Slides: https://docs.google.com/presentation/d/1AoksHoJfnrHUw59HTlMkrFDeq3UjCbmDA3n-M49y_lw/edit?usp=sharing