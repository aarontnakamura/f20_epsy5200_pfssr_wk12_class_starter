## EPSY 5200: Programming Fundamentals for Social Science Researchers
## Fall 2020 Week 12
### Web Scraping with Python

# In the latter half of class, we'll use a Python package called twint
# to scrape data from Twitter
# (the Twitter API process is laborious, so we'll use this alternative).

# Go to https://github.com/twintproject/twint

# We can link with git and pip to the GitHub for the twint project.
# On the twint page, get the URL you'd use for cloning
#  (https://github.com/twintproject/twint.git)
# and replace the https protocol with git like so:

#pip install git+git://github.com/twintproject/twint.git

# (uncomment the above line and run in terminal)

# Unfortunately, twint is not always reliable and development is a bit buggy
# This happens with open-source programming, as developers are often volunteers
# In this case, it took me some time to realize that the most recent version
#   has a couple bugs

# Here is some code I found in reading the GitHub Issues discussion (run the uncommented line)
# Note that this is a *terminal* command, not Python.

#pip install --upgrade git+https://github.com/yunusemrecatalcam/twint.git@twitter_legacy2

# now we can import packages we need
import twint
import pandas as pd
