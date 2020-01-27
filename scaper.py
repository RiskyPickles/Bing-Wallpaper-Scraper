import requests
import os
import urllib.request
from bs4 import BeautifulSoup

def manage_sources():
	wallpage1 = "https://bing.gifposter.com/archive.html"
	wallpage2 = "https://bing.gifposter.com/archive/201912.html"

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
	
	def generate_dirs_and_urls(month_list, url_list):
		for month in month_list:
			## Make new directories for each month
			dir_path = os.path.join(os.getcwd(), month)
			print (dir_path)
			# ~ os.mkdir(dir_path)
			
			## Generate URLs for each archive download source.
			base = "https://bing.gifposter.com/archive"
			url_list.append(base + "/" + month + ".html")
	
	generate_dirs_and_urls(months_2018, urls_2018)
	generate_dirs_and_urls(months_2019, urls_2019)
	
	## Checking I didn't fuck anything up in the naming of urls
	print (urls_2018)
	print (urls_2019)
	

def download():
	wallpaper_page = wallpage2
	result = requests.get(wallpaper_page)

	if result.status_code == 200:
		soup = BeautifulSoup(result.content, "html.parser")

	# ~ print (soup)
	# ~ for tag in soup.find_all("a"):
		# ~ urls.append(tag['src'])

	urls = []
	for tag in soup.find_all("img"):
		urls.append(tag['src'])
		
	urls.pop()
	# ~ print (urls)

	for count, url in enumerate(urls):
		urls[count] = url[:-3] # remove _sm from url for full size image
		name = urls[count][36:] # cut filename from domain

		print ("...Downloading " + name + " from " + urls[count])
		urllib.request.urlretrieve(
			urls[count], os.path.join(os.getcwd(), name))

def main():
	manage_sources()
	
main()
	
	
	
	
	
	
	
	
	
