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
		 