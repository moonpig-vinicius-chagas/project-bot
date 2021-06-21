from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.headless = True
#options=options
#options.add_argument("window-size=1200x600")
options.add_argument("--headless")
options.add_argument("--disable-gpu")
options.add_argument("--start-maximized")
options.add_argument("--disable-notifications")
options.add_argument("--incognito")
DRIVER_PATH = "/Users/vinicius.chagas/Documents/github/project-bot/chromedriver"

driver = webdriver.Chrome(executable_path=DRIVER_PATH)
driver.get("https://uat.moonpig.com/uk/")
#print(driver.page_source)