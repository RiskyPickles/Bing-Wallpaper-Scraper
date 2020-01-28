import requests
import os
import urllib.request
from bs4 import BeautifulSoup
import time

def main():
	sample_wallpage1 = "https://bing.gifposter.com/archive.html"
	sample_wallpage2 = "https://bing.gifposter.com/archive/201912.html"

	months_2019 = []
	months_2018 = []

	for i in range(1,13):
		if i < 10:
			months_2018.append("20180" + str(i))
			months_2019.append("20190" + str(i))
		else:
			months_2018.append("2018" + str(i))
			months_2019.append("2019" + str(i))
		
	# ~ print (months_2018)
	# ~ print (months_2019)

	urls_2019 = []
	urls_2018 = []
	
	dirs_2019 = []
	dirs_2018 = []
	
	def generate_dirs_and_urls(month_list, url_list, dir_list):
		for month in month_list:
			## Make new directories for each month
			dir_path = os.path.join(os.getcwd(), "wallpapers", month)
			dir_list.append(dir_path)
			if not os.path.exists(dir_path):
				os.mkdir(dir_path)
			
			## Generate URLs for each archive download source.
			base = "https://bing.gifposter.com/archive"
			url_list.append(base + "/" + month + ".html")
	
	generate_dirs_and_urls(months_2018, urls_2018, dirs_2018)
	generate_dirs_and_urls(months_2019, urls_2019, dirs_2019)
	
	## Checking I didn't fuck anything up in the naming of urls
	# ~ print (urls_2018)
	# ~ print (urls_2019)
	
	for url,directory in zip(urls_2018, dirs_2018):
		# ~ print (url)
		# ~ print (directory)
		download(url, directory)

def download(source_url, dest_dir):
	wallpaper_page = source_url
	result = requests.get(wallpaper_page)

	if result.status_code == 200:
		soup = BeautifulSoup(result.content, "html.parser")

	urls = []
	for tag in soup.find_all("img"):
		urls.append(tag['src'])
	urls.pop() # get rid of pesky loose data
	
	for count, url in enumerate(urls):
		urls[count] = url[:-3] # remove _sm from url for fullsize image
		name = urls[count][36:] # cut filename from domain

		print("Downloading " + name + " from " + urls[count])
		print()
		urllib.request.urlretrieve(urls[count], os.path.join(dest_dir, name))
	
main()
	
	
	
	
	
	
	
	
	
