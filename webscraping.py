import requests
import lxml
import bs4

# get the first page
# scrape the site and save the items
# get the nextPage
# if there's a nextPage
#   scrape the site and save the items
#   get the next Page

authors = set()   # make this a set so there will be unique items
quotes = set()
topTenTags = []

def scrapeSite():
    for a in soup.select("small"):
        authors.add(a.get_text())  

    for q in soup.select('.text'):
        quotes.add(q.get_text()) 

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


soup = getPage()                    # get first page
                                    # get top Ten items
for t in soup.select('.tag-item > .tag'):
    topTenTags.append(t.get_text()) 
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

print('List of Authors:')
print('---------------')
print_list(authors)
print('\nList of Quotes')
print('--------------')
print_list(quotes)
print('\nList of Top Ten Tags:')
print('---------------------')
print_list(topTenTags)

