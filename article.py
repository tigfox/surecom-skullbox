#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup
import argparse
import sys

parser = argparse.ArgumentParser()
parser.add_argument("source", help="A WAPO or NYT article to pull in from a URL.")
parser.add_argument("-d", "--dest", help="filename to save article as. defaults to print to the screen")
args = parser.parse_args()

r = requests.get(args.source)
soup = BeautifulSoup(r.text, "html.parser")
url_list = args.source.split(".")
if "nytimes" in url_list:
	article = soup.find('section',{'name':'articleBody'}) # NYT
elif "washingtonpost" in url_list:
	article = soup.find('div',{'class':'article-body'}) # WAPO
else:
	print("WAPO and NYT are currently the only sites supported.")
	sys.exit()
article_text = article.find_all(text=True)
article_links = article.find_all('a')

if not args.dest:
	print("No destination provided, printing to screen")
	print(soup.title)
	for line in article_text:
		print(line)
	# for link in article_links:
	# 	print([t for t in link.find_all(text=True) if t.parent.name == 'a'])
else:
	# write some file handing stuff here and then print the text to it
	pass