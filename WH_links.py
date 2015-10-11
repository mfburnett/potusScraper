import requests
import bs4

root_url = 'https://www.whitehouse.gov'
index_url = root_url + '/briefing-room/speeches-and-remarks'

def get_urls(page_num):
    response = requests.get(index_url+'?page='+str(page_num))
    soup = bs4.BeautifulSoup(response.text)
    items = soup.select('li.views-row h3 a')
    return [root_url + a.attrs.get('href') for a in items]

# Looping through base urls to pull every link from every page (1-357) in the system.
for x in xrange(0,357):
	urls = ','.join(get_urls(x))
	requests.post('http://52.6.45.46:4151/pub?topic=whurls', urls)
	print urls