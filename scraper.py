from urllib.request import Request, urlopen
from bs4 import BeautifulSoup as soup




def price(item):

	item_url = item.replace(" ","_")

	url = Request("https://oldschool.runescape.wiki/w/{0}".format(item_url), headers={'User-Agent': 'Mozilla/5.0'})
	
	try:
		client = urlopen(url)

	except:
		return("Invalid item")

	html = client.read()
	client.close

	page_soup = soup(html, "html.parser")
	price = page_soup.find("span",{"class":"infobox-quantity-replace"})
	name = page_soup.h1
	print("{0} is worth {1}gp!".format(name.get_text(),price.get_text()))
	return("{0} is {1}gp on the Grand Exchange! :moneybag:".format(name.get_text(),price.get_text()))


def wiki(thing):
	thing_url = thing.replace(" ","_")


	str_url = "https://oldschool.runescape.wiki/w/{0}".format(thing_url)
	url = Request("https://oldschool.runescape.wiki/w/{0}".format(thing_url), headers={'User-Agent': 'Mozilla/5.0'})
	try:
		client = urlopen(url)
		client.close
		return(str_url)

	except:
		return("Invalid query :x:")