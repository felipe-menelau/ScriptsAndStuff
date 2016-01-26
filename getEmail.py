from bs4 import BeautifulSoup, SoupStrainer
import requests
import requests.exceptions
from urllib.parse import urlsplit
from collections import deque
import re

def emails(para): 
	new_urls = deque([para])
	print (new_urls)
	processed_urls = set()
	e = open("email2.txt", 'a+')
	f = open("facebook.txt", 'a+')

 
	emails = set()
	facebook = set()
 
	for x in range(0, 20):
		if not new_urls:
			break
		url = new_urls.popleft()
		processed_urls.add(url)

		parts = urlsplit(url)
		base_url = "{0.scheme}://{0.netloc}".format(parts)
		path = url[:url.rfind('/')+1] if '/' in parts.path else url
 
		print("Processing %s" % url)
		try:
			s = requests.Session()
			s.headers['User-Agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.131 Safari/537.36'
			response = s.get(url)
		except (requests.exceptions.MissingSchema, requests.exceptions.ConnectionError, requests.exceptions.InvalidURL):
			continue
 
		new_emails = set(re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", response.text, re.I))
		emails.update(new_emails)
 
		soup = BeautifulSoup(response.text)
 
		for anchor in soup.find_all("a"):
			link = anchor.attrs["href"] if "href" in anchor.attrs else ''
			if link.startswith('/'):
				link = base_url + link
			elif not link.startswith('http'):
				link = path + link
			if ("facebook" in link or "linkedin" in link or "twitter" in link):
				with open('facebook.txt', 'a+') as f:
					for line in f:
						if link in line:
							break
					else:
							f.write(link+'\n')
			if not link in new_urls and not link in processed_urls:
				new_urls.append(link)

	e.write(str(emails) + '\n')


f = open("espanholsvalidos.txt", 'r')

for x in range (0, 10):
	emails(f.readline().rstrip())