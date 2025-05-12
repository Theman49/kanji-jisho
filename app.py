import requests
from bs4 import BeautifulSoup

result = ''
level = 'n4'
for i in range(1,10):
	filename = "./data/" + level + "_page_" + str(i) + ".html"
	r = requests.get('https://jisho.org/search/%23kanji%20%23jlpt-' + level + '?page=' + str(i))
	print(r)

	soup = BeautifulSoup(r.content, 'html.parser')
	content = soup.find('div', {'id':'page_container'})
	result += str(content)

	#write result into file
	with open(filename, "a") as f:
		f.write(str(content))

	print('Scraping Page', i, 'DONE')

filename = "./data/" + level + "_all.html"
with open(filename, "a") as f:
	f.write(str(result))