## Google images thumbnails scrapper (without api)

import dryscrape
import os
try:
    from urllib.request import urlretrieve  # Python 3
except ImportError:
    from urllib import urlretrieve  # Python 2

search_term = input("Enter key word for images: ")
print ("downloading requested images...")

# set up a web scraping session
sess = dryscrape.Session(base_url = 'http://images.google.com')

# visit homepage and search for a term
sess.visit('/')
q = sess.at_xpath('//*[@name="q"]')
q.set(search_term)
q.form().submit()

# create list of images sources links
linki = []
for link in sess.xpath('//img[@src]'):
    linki.append(link['src'])
    
# check if search_term directory exists... create if not
os.chdir(os.path.dirname(os.path.abspath(__file__)))

if not os.path.exists('images/' + search_term):
    os.makedirs('images/' + search_term)

mydir = 'images/' + search_term  + '/'
print (mydir)
    
# go through links list and download each picture to created directory
n = 1
for link in linki:
    n = n+1
    try:
        urlretrieve(link, mydir + search_term + str(n) + '.jpg')
    except:
        pass
    
# this is it
print ("You entered: ", search_term, " - your pictures have been downloaded.")
