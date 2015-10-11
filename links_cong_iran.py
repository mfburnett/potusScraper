import requests
import bs4

root_url = 'https://www.congress.gov'
index_url = root_url + '/search?q=%7B"source"%3A"legislation"%2C"search"%3A"iran"%2C"congress"%3A%5B"114"%2C"113"%2C"112"%2C111%5D%7D&pageSort=dateOfIntroduction%3Adesc&pageSize=250'

def get_urls(page_num):
    response = requests.get(index_url+"&page="+str(page_num))
    soup = bs4.BeautifulSoup(response.text)
    items = soup.select('ul.results_list li h2 a')
    return [a.attrs.get('href') for a in items]

# Looping through base urls to pull every link from every page (1-357) in the system.
for x in xrange(1,2):
	urls = ','.join(get_urls(x))
	requests.post('http://52.6.45.46:4151/pub?topic=congress', urls)
	print urls