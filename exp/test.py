import requests
from bs4 import BeautifulSoup
import cfscrape
import re

scraper = cfscrape.create_scraper()
url = 'https://rj.olx.com.br/rio-de-janeiro-e-regiao/imoveis/apartamento-de-2-quartos-na-barra-da-tijuca-812795532'


def bypassScraper(link):
    """Bypass the bot defense"""
    my_str_value = scraper.get(link).content
    my_str_value_decoded = my_str_value.decode("utf-8")
    return my_str_value_decoded


def soupFunction(url):
    """Function to acces the link"""
    return BeautifulSoup(bypassScraper(url), 'html.parser')

def findChat(soup):
    """Function to find price"""
    chat = soup.find_all('div', attrs={'class': 'sc-hmzhuo sc-1ukaq78-0 kdUfgo sc-jTzLTM iwtnNi'})
    return chat

#a = soupFunction(url)
#print(a.find("button"))

print(findChat(soupFunction(url)))


#if __name__ == "__main__":
#    for x,y,z in zip(findPrice(soupFunction(url)), findAddress(soupFunction(url)), findLink(soupFunction(url))):
#        print("price {} and house {} and link {} ".format(x.get_text(),y.get_text(),z.attrs['href']))

