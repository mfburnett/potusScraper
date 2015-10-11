import requests
import bs4
import csv
import re
from bs4 import BeautifulSoup as soup, Tag

root_url = 'https://www.congress.gov'
index_url = root_url + '/search?q=%7B"source"%3A"legislation"%2C"search"%3A"cuba"%2C"congress"%3A%5B"114"%2C"113"%2C"112"%2C111%5D%7D&pageSort=dateOfIntroduction%3Adesc&pageSize=250'

# Get url of each bill.
def get_urls(page_num):
    response = requests.get(index_url+"&page="+str(page_num))
    soup = bs4.BeautifulSoup(response.text)
    items = soup.select('ul.results_list li h2 a')
    return [a.attrs.get('href') for a in items]

# Looping through base urls to pull every link from each page.
all_url1 = ','.join(get_urls(1))
all_url2 = ','.join(get_urls(2))
url1 = str(all_url1).split(',')
url2 = str(all_url2).split(',')
for i in url1:
	print i
for i in url2:	
	print i

# Get bill title.
def get_titles(page_num):
	response = requests.get(index_url+"&page="+str(page_num))
	soup = bs4.BeautifulSoup(response.text)
	title = soup.select('.results_list li h2 a')
	
	for i in title:
		print i.getText()

get_titles(1)
get_titles(2)

# Get sponsor, party, and date introduced for each bill. 
def get_sponsor_party_date(page_num):
	response = requests.get(index_url+"&page="+str(page_num))
	soup = bs4.BeautifulSoup(response.text)
	for spd in soup.findAll(text='Sponsor:'):
		for item in spd.parent.next_siblings:
			if isinstance(item, Tag):
				# Get sponsor.
				print str(item.text).split(']')[0]
				# Get party.
				print str(item.text).split('[')[1].split('-')[0]
				# Get date.
				print str(item.text).split('(')[1].split(' ')[1].split(')')[0]

get_sponsor_party_date(1)
get_sponsor_party_date(2)