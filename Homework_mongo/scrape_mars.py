from splinter import Browser
from bs4 import BeautifulSoup
import pandas as pd

def iiniciar_browser(): 
    exec_path = {'executable_path': 'chromedriver'}
    return Browser('chrome', headless=True, **exec_path)

dict_mars={}

def nasa_mars_news():
	browser = iiniciar_browser()
	url = "https://mars.nasa.gov/news/"
	browser.visit(url)
	html = browser.html
	soup = BeautifulSoup(html, "html.parser")
	article = soup.find("div", class_='list_text')
	title = article.find("div", class_="content_title").text
	text = article.find("div", class_ ="article_teaser_body").text
	#agregar datos a diccionario
	dict_mars['title'] =title
	dict_mars['text']=text
	browser.quit()
	return dict_mars


def featured_image_url():
	browser = iiniciar_browser()
	url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars" 
	browser.visit(url)
	html = browser.html
	soup = BeautifulSoup(html, "html.parser")
	img_path = soup.find("img", class_="thumb")["src"]
	featured_image_url  = "https://www.jpl.nasa.gov/"+img_path
	dict_mars['featured_image_url'] = featured_image_url
	browser.quit()
	return dict_mars

def mars_weather():
	browser = iiniciar_browser()
	url = "https://publish.twitter.com/?query=https%3A%2F%2Ftwitter.com%2FMarsWxReport%2Fstatus%2F1235623906687533057&widget=Tweet" 
	browser.visit(url)
	html = browser.html
	soup = BeautifulSoup(html, "html.parser")
	temp_tweet = soup.find("blockquote", class_="twitter-tweet")
	mars_weather=temp_tweet.text
	dict_mars['mars_weather']=mars_weather
	browser.quit()
	return dict_mars

def Mars_facts():
	browser = iiniciar_browser()
	url = "https://space-facts.com/mars/" 
	browser.visit(url)
	html = browser.html
	soup = BeautifulSoup(html, "html.parser")
	table_mars = soup.find("table", class_="tablepress tablepress-id-p-mars",id="tablepress-p-mars")
	tables = pd.read_html(url)
	df = tables[0]
	df.columns = ['Metric', 'Data']
	df.set_index('Metric', inplace=True)
	html_table=df.to_html()
	dict_mars['Mars_facts']=html_table
	browser.quit()
	return dict_mars

def Mars_Hemispheres():
	browser = iiniciar_browser()
	url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars" 
	browser.visit(url)
	html = browser.html
	soup = BeautifulSoup(html, "html.parser")
	Mars_hemispheres = soup.find_all('div', class_='item')
	info_Mars_hemispheres=[]
	for x in Mars_hemispheres:
		title = x.find("h3").text
		title = title.replace("Enhanced", "")
		url_fullimage = x.find("a")["href"]
		image_link = "https://astrogeology.usgs.gov/" + url_fullimage
		browser.visit(image_link)
		html = browser.html
		soup=BeautifulSoup(html, "html.parser")
		downloads = soup.find("div", class_="downloads")
		image_url = downloads.find("a")["href"]
		info_Mars_hemispheres.append({"title": title, "img_url": image_url})
	dict_mars['Mars_Hemispheres'] = info_Mars_hemispheres
	browser.quit()
	return dict_mars

