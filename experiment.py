from urllib import urlopen
from bs4 import BeautifulSoup
import re

webpage = urlopen('https://www.nytimes.com/').read()

title = re.compile('html">(.*)</a></h2>')

link = re.compile('<h2 class="story-heading"><a href="(.*)">')

#make list of titles and links in the webpage
findTitle = re.findall(title,webpage)
findLink = re.findall(link,webpage)

listIterator = []
listIterator[:] = range(0,5)

for i in listIterator:
	print findTitle[i]
	print findLink[i]

