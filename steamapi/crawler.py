import requests
import urllib
import re
import time
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
import secrets
import html2text

pd.set_option('display.max_columns', None)

# Returns pandas array of reviews from requested steam url.
def get_reviews(url):
	# Keeps track of number of reviews.
	review_num = 0

	# Requests from Steamworks API and crawls page.
	for i in range(0, 1):
		new_url = _get_request_url(url, i)
		page = requests.get(new_url)
		soup = BeautifulSoup(page.content, 'html.parser')
		# Cleaning all the excessive \t and \n from API response.
		clean_text = page.text.replace('\\t', '').replace('\\n', '').replace('\\r', '').replace('\\/', '/')
		html_text = html2text.html2text(clean_text)
		print(html_text)

		# Adds time to not overstress servers, following Steam guidelines of 200 requests per 5 minute.
		time.sleep(2)

	print("Finished recording " + str(df.shape[0]) + " reviews.")
	return

# Stores pandas array into filename specified.
def store_reviews(df, filename):
	df.to_csv(filename)
	print("Successfully stored!")

# Returns the request url for the nth page of reviews.
def _get_request_url(url, n):
	n = str(n * 20)
	return url + n

get_reviews(secrets.dota_url)
#store_reviews(get_reviews(secrets.dota_url), secrets.dota_file)
#store_reviews(get_reviews(secrets.pubg_url), secrets.pubg_file)
#store_reviews(get_reviews(secrets.csgo_url), secrets.csgo_file)
