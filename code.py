# web_spider

import request
from bsh import BeautifulSoup

def trade_spider(max_pages):
	page = 1
	while page < max_pages:

		url = 'www.anything.com' + str(page)
		source_code = request.get(url)
		plain_text = source_code.txt 
		Soup = BeautifulSoup(plain_text)
		for link in Soup.findAll('a',{'class:'item name'}):
			href = "www.main_url.com" + link.get('href')
			title = link.string 


			get_single_item_data(href)
			page +=1

def get_single_item_data(item_url):
	
	source_code = request.get(item_url)
	plain_text = source_code.txt
	Soup = BeautifulSoup(plain_text)
	for item_name in Soup.find('div',{'class':'i-name'}):
		print(item_name).string


trade_spider(4)

		 	 