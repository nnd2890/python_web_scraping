from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen('https://en.wikipedia.org/wiki/Kevin_Bacon')
bsObj = BeautifulSoup(html, 'lxml')
for link in bsObj.findAll('a'):
    if 'href' in link.attrs:
        print(link.attrs['href'])