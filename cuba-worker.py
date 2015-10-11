import requests
import bs4
import nsq
import csv

def handler(message):
# Isolate body of text that I want in website.
	speech_arr = message.body.split(',')
	print speech_arr
	for x in speech_arr:
		response = requests.get(x)
		soup = bs4.BeautifulSoup(response.text)
		items = soup.select('#content p')
		words_cuba = ['Cuba','trade','embargo','Havana','Castro','communism','diplomacy']
# Store date and total number of times any of the words in the set occurs in the speech.
		occurences = 0
		for y in items:	
			for w in words_cuba:
				occurences += str(y).count(w)
		space_date = str(soup.select('div.date'))
		date = space_date[32:50]
		with open('whurls_cuba.csv', 'a') as f:
			a = csv.writer(f, delimiter=',')
			data = [[date, occurences]]
			a.writerows(data)
			f.close()
	
	message.touch()
	message.finish()

# Reads the messages coming through the queue.
reader = nsq.Reader(message_handler=handler, nsqd_tcp_addresses=['52.6.45.46:4150'], 
					topic = 'whurls', channel='channel_cuba', output_buffer_timeout=0)

nsq.run()