from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen('http://pythonscraping.com/pages/page3.html')
bsObj = BeautifulSoup(html,'lxml')
images = bsObj.findAll('img',{'src':re.compile(r"\.\.\/img\/gifts/img.*\.jpg")})
for image in images:
    print(image['src'])