import requests
import bs4
import nsq

root_url = 'https://www.whitehouse.gov'
index_url = root_url + '/briefing-room/speeches-and-remarks'

# Pulling all the page urls from the White House's website.
# Hardcoded it to save time.

def get_urls(page_num):
    response = requests.get(index_url+'?page='+str(page_num))
    soup = bs4.BeautifulSoup(response.text)
    items = soup.select('li.views-row h3 a')
    return [root_url + a.attrs.get('href') for a in items]

