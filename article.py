#!/usr/bin/env python3

import sys
import requests
from bs4 import BeautifulSoup
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("source", help="a wapo article to pull, in the form of a URL")
parser.add_argument("destination", help="filename to save article as. defaults to print to the screen")
args = parser.parse_args()

if not args.source:
	print("You must provide a source URL")
	sys.exit()

r = requests.get(args.source)
soup = BeautifulSoup(r.text, "html.parser")
article = soup.find('div',{'class':'article-body'})
article_text = article.find_all(text=True)

if not args.destination:
	print("No destination provided, printing to screen")
	print(soup.title)
	for line in article_text:
    	print(line)
else:
	# write some file handing stuff here and then print the text to it