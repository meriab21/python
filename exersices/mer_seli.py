from selenium import webdriver
import time
import random
from selenium.webdriver.common.keys import Keys

first_delay=random.randint(1,3)
second_delay=random.randint(2,4)





chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.geolocation": 2}
chrome_options.add_experimental_option("prefs", prefs)
chrome_options.add_argument("--disable-infobars")
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--disable-notifications")
chrome_options.add_argument("--disable-popup-blocking")
chrome_options.add_argument("--incognito")
driver = webdriver.Chrome("C:/Users/Meron/Desktop/meri/chromedriver", options=chrome_options)

print(first_delay)
time.sleep(first_delay)

driver.get('http://www.pcgministry.epizy.com/')
body = driver.find_element_by_tag_name('body')
body.send_keys(Keys.DOWN)
print(second_delay)
time.sleep(second_delay)
a = driver.find_element_by_xpath("//h2[contains(text(),'ABOUT US')]"
    )
# print(a.text)

b = driver.find_element_by_xpath("//body[1]/div[2]/div[2]/div[1]/div[1]/div[1]/span[1]")
print(a.text, b.text)
file = open("seli.txt", "w")
file.write(a.text)
file.write(b.text)
file.close()



