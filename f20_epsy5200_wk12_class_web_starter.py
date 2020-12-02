## EPSY 5200: Programming Fundamentals for Social Science Researchers
## Fall 2020 Week 12
### Web Scraping with Python

# First, make sure you install the BeautifulSoup package
# Run this in the command line (uncommented):
#python3 -m pip install --user BeautifulSoup


from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup
# this just loads all fxns and attaches their names to our enviro
# in other words, no need to use the package name

# some functions adapted from RealPython demo:
# https://realpython.com/python-web-scraping-practical-introduction/

def simple_get(url):
    """
    Attempts to get the content at `url` by making an HTTP GET request.
    If the content-type of response is some kind of HTML/XML, return the
    text content, otherwise return None.
    """
    try: # make an attempt to do this, but if there's an ERROR, jump to the "except"
        with closing(get(url, stream=True)) as resp:
            if is_good_response(resp): # calls function defined below
                return resp.content
            else:
                return None
    except RequestException as e: # only runs if error occurs above
        log_error('Error during requests to {0} : {1}'.format(url, str(e)))
        return None


def is_good_response(resp):
    """
    Returns True if the response seems to be HTML, False otherwise.
    """
    content_type = resp.headers['Content-Type'].lower()
    return (resp.status_code == 200 # remember that 200 means all OK!
            and content_type is not None # makes sure there's *something* in content
            and content_type.find('html') > -1)


def log_error(e): # just in case error above, prints it
    """
    It is always a good idea to log errors.
    This function just prints them, but you can
    make it do anything.
    """
    print(e)


# let's get scraping!
raw = simple_get("http://blogs.edweek.org/edweek/inside-school-research/")
