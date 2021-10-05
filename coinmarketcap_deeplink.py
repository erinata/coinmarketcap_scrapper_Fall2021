import urllib.request
import os 
import time

import pandas


if not os.path.exists("deep_link_html"):
	os.mkdir("deep_link_html")


df = pandas.read_csv("parsed_files/coinmarketcap_dataet.csv")

# print(df)
for link in df['link']:
	file_name = link.replace("/currencies/","").replace("/","")
	print(file_name)
	f = open("deep_link_html/coinmarketcap_" + file_name + ".html", "wb")
	response = urllib.request.urlopen("http://coinmarketcap.com" + link)
	html = response.read()
	f.write(html)
	f.close()
	time.sleep(30)



