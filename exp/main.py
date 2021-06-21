import requests
from bs4 import BeautifulSoup
import cfscrape
import re
from util import open_browser, login, chat_msg, save_json, read_json, change_url, find_main_pages
import time
import json


"""Global Variables"""
count_pages = 0
site_list = []
temp_list = []


scraper = cfscrape.create_scraper()
#url = 'https://www.olx.com.br/imoveis/venda?f=p&q=barra%20da%20tijuca'
#page2= 'https://www.olx.com.br/imoveis/venda?f=p&o=2&q=barra%20da%20tijuca'


def bypassScraper(link):
    """Bypass the bot defense"""
    my_str_value = scraper.get(link).content
    my_str_value_decoded = my_str_value.decode("utf-8")
    return my_str_value_decoded


def findAddress(soup):
    """Function to find address within main page"""
    address = soup.find_all('div', attrs={'class': 'fnmrjs-6 iNpuEh'})
    return address


def findPrice(soup):
    """Function to find price"""
    price = soup.find_all('div', attrs={'class': 'sc-hmzhuo sc-1iuc9a2-7 CYgas sc-jTzLTM iwtnNi'})
    return price


def findLink(soup):
    """Function to find link throughout the page"""
    link = soup.find_all('a', attrs={'data-lurker-detail': 'list_id'})
    return link


def soupFunction(url):
    """Function to access the link and return html file ready to be parsed"""
    return BeautifulSoup(bypassScraper(url), 'html.parser')


def find_embedded_urls(url):
    """Return embedded urls for each main page and return in a list"""
    
    # 4 - Gather embedded Urls from main pages and save it to the list site_list to be used for comparison by 'main_function'.
    
    site_list.clear() #empty the site_list every time this function runs

    for t in findLink(soupFunction(url)):
        site_list.append(t.attrs['href'])
    
    site_list_total = len(site_list)

    #save_json(site_list, 'data.json') #save site_list into a data.json file for further comparison (not needed)
    print('-'*150 + '\n' + '-'*150)
    print('[+][find_embedded_urls] Printing embedded urls found for the main page: ', url)
    print('[+][find_embedded_urls] A total of : ' + str(site_list_total) + ' apartments have been found.')
    print('\n'*2, site_list)

    return site_list


def main_function(lista):
    
    # 5 
    # 'find_embedded_urls' function returns a list of embedded urls found on each main page.
    # The code below will execute each embedded url found in the list
    # The code Initializes the stored_sites.json to check if any of the embeddered Urls in the list were already been used in the past.
    # For each embedded_url from a main page, compare if that Url was already used by the program or not
    # If the URl is already present in the read_from_stored_json then the code is not executed
    # Else execute the code and append the URL into the read_from_stored_json list
    # Once the for ends, the read_from_stored_json list is written at stored_sites.json and in the next time this loop run again, the list is running again with the latest URls.

    #saved_json = read_json('data.json') # read from site_list list. (not needed)
    read_from_stored_json = read_json('stored_sites.json') 
    count = 0
    site_list_total = len(lista)

   

    for x in lista[:1]: 
        count = count + 1

        if x in read_from_stored_json:
            print('\n'*2 + '-'*10 + 'Warning!!!' + '-'*10)
            print(x)
            print('[+][main_function] This url was already executed and will not be executed:')
            print(str(count) + '/' + str(site_list_total) + ' ' + x, '\n')
            

            
        else:
            print('\n[+][main_function] Executing login to the Url:' + x)
            print(str(count) + '/' + str(site_list_total) + ' ' + x, '\n')
            
            time.sleep(3)
            a = login(open_browser(x))
            read_from_stored_json.append(x)
            #chat_msg(a)
            #open_browser(x)

    save_json(read_from_stored_json, 'stored_sites.json') # Only enabled this line when the code goes to prod.


#MAIN CODE EXECUTION:
# 1 - Check for the main pages using the function list_main_pages
print('\n'*50 + '[+] Starting main code execution...\n')
list_main = find_main_pages(1) # 2
print('[+][find_main_pages] Finding main URL pages as per argument and return it through the list: list_main_pages...\n ')
print('[+][find_main_pages] Printing main pages found in a list...\n', list_main)

# 3 For each main page in the list_main, find the embedded pages
for site_main in list_main:
    main_function(find_embedded_urls(site_main))
    time.sleep(3)
    







    








#if __name__ == "__main__":
#    for x,y,z in zip(findPrice(soupFunction(url)), findAddress(soupFunction(url)), findLink(soupFunction(url))):
#        print("price {} and house {} and link {} ".format(x.get_text(),y.get_text(),z.attrs['href']))
