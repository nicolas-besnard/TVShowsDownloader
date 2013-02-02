import os
import urllib2
from bs4 import BeautifulSoup

def get_page_content(url):
	try:     
		website = urllib2.urlopen(url)
	except urllib2.HTTPError, e:     
		print "Cannot retrieve URL: HTTP Error Code", e.code 
		return False
	except urllib2.URLError, e:     
		print "Cannot retrieve URL: " + e.reason[1] 
		return False
	content = website.read()
	website.close()
	return content

def download_magnet(url):
	url = urllib2.unquote(url)
	os.startfile(url)

def getListLink(name, cat = 0):
	listCat = {}
	listCat[0] = 0 #all
	listCat[1] = 208 #seriehd
	seekCat = listCat[cat]
	url = "http://thepiratebay.se/search/"+ name +"/0/7/"+ str(seekCat)
	return url

def getInfos(name, cat = 0):
	
	content = get_page_content(getListLink("arrow"))
	dom = BeautifulSoup(content)
	get_table = dom.find('table', id="searchResult")


	get_tr = get_table.findAll('tr')
	for tr in get_tr:
		get_cat = tr.a
		get_subCat = get_cat.find_next("a")
		get_name = get_subCat.find_next("a")
		get_link = get_name.find_next("a")
		get_seeders = tr.find('td', {"align" : "right"})
		cat = get_cat.contents[0]
		subCat = get_subCat.contents[0]

		###############################################################################
		if (cat == "  Click here to download." or cat == "Type"): # TODO : fix this shit
			continue		
		###############################################################################

		name = get_name.contents[0]		
		link = get_link["href"]		
		seeders = str(get_seeders).split('<')[1].split('>')[1]
		print seeders

print getInfos("arrow")

