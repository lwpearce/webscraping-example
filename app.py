import requests
import lxml
import bs4
from flask import Flask

app = Flask(__name__)
    
# get the first page
# scrape the site and save the items
# get the nextPage
# if there's a nextPage
#   scrape the site and save the items
#   get the next Page

authors = []
quotes = []
topTenTags = []

def scrapeSite():
    for a in soup.select("small"):
        if (a.get_text() not in authors):
            authors.append(a.get_text())

    for q in soup.select('.text'):
        if (q.get_text() not in quotes):
            quotes.append(q.get_text())

    for t in soup.select('.tag-item > .tag'):
        if (t.get_text() not in topTenTags):
            topTenTags.append(t.get_text()) 

def print_list(listToPrint):
    for l in listToPrint:
        print(l)

def anotherPage(nextTag):
    if len(nextTag) == 0:
        return False
    return True

def getPage(page = ''):
    res = requests.get(f"http://quotes.toscrape.com{page}")
    return bs4.BeautifulSoup(res.text,"lxml")

@app.route("/")
def home():
    soup = getPage()                    # get first page
    scrapeSite()                        # scrape the first page 
    next_tag = soup.select('.next a')   # get the next page tag  
    if len(next_tag) == 0:              # if there's no next page,
        keepGoing = False               # don't keep going
    else:
        keepGoing = True
        nextPage = next_tag[0].get_attribute_list('href')[0]

    while keepGoing:       

        soup = getPage(nextPage)            # get the soup of the next page
        scrapeSite()                        # scrape the next page
        next_tag = soup.select('.next a')   # get the next page tag  

        if len(next_tag) == 0:              # if there's no next page,
            keepGoing = False               # don't keep going
        else:
            keepGoing = True
            nextPage = next_tag[0].get_attribute_list('href')[0]

            print_list(authors)
            print_list(quotes)
            print_list(topTenTags)

    return "Hey, Flask!"

