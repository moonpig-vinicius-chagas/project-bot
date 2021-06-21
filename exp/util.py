#importing webdriver from selenium 
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium import webdriver   # for webdriver
from selenium.webdriver.chrome.options import Options  # for suppressing the browser
import time
import os
import yaml 
import json

#selecting Firefox as the browser 
#in order to select Chrome 
# webdriver.Chrome() will be used 

#URL of the website 
#url = "https://rj.olx.com.br/rio-de-janeiro-e-regiao/imoveis/apartamentos-na-barra-da-tijuca-816883291"
home = 'https://www.olx.com.br/imoveis/venda?f=p&q=barra%20da%20tijuca'


def return_chromedriver_dir():
    '''Find out directory where 'chromedriver file is and return the dir'''
    for dirpath, dirname, filenames in os.walk(os.getcwd()):
        if 'chromedriver' in filenames:
            return dirpath + '/chromedriver'
        else:
            pass
        
option = webdriver.ChromeOptions()
option.add_argument("window-size=1200x600")
option.add_argument('--disable-gpu')
option.add_argument('--headless')
option.add_argument('--disable-extensions')
option.add_argument('--disable-logging')
option.add_argument('--ignore-certificate-errors')
# driver = webdriver.Chrome(executable_path = f'{return_chromedriver_dir()}', options=option) 
driver = webdriver.Chrome(executable_path = f'{return_chromedriver_dir()}') 

def open_browser(url):       
    '''#opening link in the browser and click chat '''
    driver.get(url)
    #content = driver.find_elements_by_class_name('sc-blIhvV dWPUbU sc-jTzLTM iwtnNi')
    pages = driver.find_elements_by_xpath("//*[@class='sc-blIhvV dWPUbU sc-jTzLTM iwtnNi']")
    #pages = driver.find_elements_by_xpath('//*[@id="miniprofile"]/div/div/div[5]/div/div/div[1]/div/div')
    for e in pages:
        print(e)
        return e.click()


def login(pages):
    '''Loging '''
    with open(r'info.yml') as file:
        documents = yaml.full_load(file)
        print(documents['credential']['user'])
    time.sleep(2)
    try:
        username = driver.find_element_by_css_selector("input[type='email']")
        password = driver.find_element_by_css_selector("input[type='password']")
        username.send_keys(documents['credential']['user'])
        password.send_keys(documents['credential']['pass'])
        time.sleep(2)
        #login_button = driver.find_elements_by_xpath("//button[text()='text']")
        pages = driver.find_elements_by_xpath('//*[@id="__next"]/div/div/div[1]/div[2]/form/button')
        time.sleep(0.5)
        return pages[0].click()
    except:
        pass
    

def chat_msg(chat):
    ''' Send msg to chat'''
    text = "Desculpa, foi sem querer"
    time.sleep(5)
    #Find element with no S
    chat_area = driver.find_element_by_xpath('//*[@id="mercurie-app"]/div/div/div/div/div/div/div[3]/div[1]/div[4]/textarea')
    button = driver.find_elements_by_xpath('//*[@id="mercurie-app"]/div/div/div/div/div/div/div[3]/div[1]/div[4]/div[2]/div')
    print(button)
    chat_area.send_keys(text)
    button[0].click()


def save_json(save_list, name_json):
    """Function to save file in json"""
    with open(name_json, 'w') as outfile:
        json.dump(save_list, outfile)


def read_json(name_json):
    """Function to return a list in a variable the user choose"""
    with open(name_json, 'r+') as json_file:
        data = json.load(json_file)
        return data


def change_url(url):
    '''return the next page than the one provided'''
    driver.get(url)
         
    main = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "Próxima pagina"))
    )
    main.click()
    time.sleep(3)
    return driver.current_url


def find_main_pages(x):
    '''return the main pages in a list total_main_sites'''
    # 2 - User has to provide as argument to 'x' how many main pages he wants the crawler executes

    total_main_sites = ['https://www.olx.com.br/imoveis/venda?f=p&q=barra%20da%20tijuca&sf=1']

    for i in range(x):
        next_page = change_url(total_main_sites[-1])
        time.sleep(3)
        total_main_sites.append(next_page)
    
    return total_main_sites


        

    

    



    

    


    

'''Checking number of lines in the list, now its shows 500
Sometimes open 2 pages, one for login other sms (Check SMS its over if youse VPN to brasil)
To fix usingg TRY
try to login, if no find email move to the next one
if not find this Unable to locate element: {"method":"css selector","selector":"input[type='email']"} move to next phase
//*[@id="mercurie-app"]/div/div/div/div/div/div/div[3]/div[1]/div[4]/textarea
'''