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

# for i in listIterator:
# 	print findTitle[i]
# 	print findLink[i]


webpage2 = urlopen('https://www.nytimes.com/2017/12/31/business/high-tax-states-law.html?hp&action=click&pgtype=Homepage&clickSource=story-heading&module=first-column-region&region=top-news&WT.nav=top-news').read()
soup2 = BeautifulSoup(webpage2, "lxml")
titleSoup = soup2.findall('title')

for i in listIterator:
	print titleSoup[i]
	#print linkSoup[i]
	print "\n"



