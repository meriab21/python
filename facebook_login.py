from selenium import webdriver
import time
import random
from selenium.webdriver.common.keys import Keys

first_delay = random.randint(1, 3)
second_delay = random.randint(2, 4)
one_sec_delay = random.randint(4, 5)
third_delay = random.randint(5, 6)
fouth_delay = random.randint(6, 9)

chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.geolocation": 2}
chrome_options.add_experimental_option("prefs", prefs)
chrome_options.add_argument("--disable-infobars")
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--disable-notifications")
chrome_options.add_argument("--disable-popup-blocking")
chrome_options.add_argument("--incognito")
driver = webdriver.Chrome(
    "C:/Users/Meron/Desktop/meri/chromedriver", options=chrome_options)
print(first_delay)
time.sleep(first_delay)

driver.get('https://www.facebook.com/')
# body = driver.find_element_by_tag_name('body')
print(second_delay)
time.sleep(second_delay)

tih = "tigi.solomon.752"
for x in tih:
    one_sec_delay = random.randint(0, 1)
    print(one_sec_delay)
    time.sleep(one_sec_delay)
    driver.find_element_by_xpath("//input[@id='email']").send_keys(x)


print(second_delay)
time.sleep(second_delay)

passw = "sheldon1@et"
for p in passw:

    one_sec_delay = random.randint(1, 2)
    print(one_sec_delay)
    time.sleep(one_sec_delay)
    driver.find_element_by_xpath("//input[@id='pass']").send_keys(p)


time.sleep(third_delay)
driver.find_element_by_xpath(
    "//body[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/form[1]/div[2]/button[1]").click()
time.sleep(fouth_delay)
body = driver.find_element_by_tag_name('body')
screen_height = driver.execute_script("return window.screen.height")
i = 1
while True:
    count=0
    first_delay = random.randint(1, 3)
    second_delay = random.randint(2, 4)
    one_sec_delay = random.randint(4, 5)
    third_delay = random.randint(5, 6)
    fouth_delay = random.randint(6, 9)
    body = driver.find_element_by_tag_name('body')
    body.send_keys(Keys.ARROW_DOWN)
    time.sleep(one_sec_delay)
    body.send_keys(Keys.PAGE_DOWN)
time.sleep(second_delay)~
    body.send_keys(Keys.ARROW_UP)
    time.sleep(first_delay)
    if int(first_delay)% 2 ==0:
        time.sleep(one_sec_delay)
        body.send_keys(Keys.PAGE_DOWN)
        time.sleep(second_delay)
        body.send_keys(Keys.PAGE_UP)
        time.sleep(first_delay)
    share_buttons = driver.find_elements_by_class_name(
        "oajrlxb2.gs1a9yip.g5ia77u1.mtkw9kbi.tlpljxtp.qensuy8j.ppp5ayq2.goun2846.ccm00jje.s44p3ltw.mk2mc5f4.rt8b4zig.n8ej3o3l.agehan2d.sk4xxmp2.rq0escxv.nhd2j8a9.mg4g778l.pfnyh3mw.p7hjln8o.kvgmc6g5.cxmmr5t8.oygrvhab.hcukyx3x.tgvbjcpo.hpfvmrgz.jb3vyjys.rz4wbd8a.qt6c0cv9.a8nywdso.l9j0dhe7.i1ao9s8h.esuyzwwr.f1sip0of.du4w35lb.n00je7tq.arfg74bv.qs9ysxi8.k77z8yql.pq6dq46d.btwxx1t3.abiwlrkh.p8dawk7l.lzcic4wl")
    try:
        for share_button in share_buttons:
            checker_share = share_button.get_attribute("aria-label")
            print(checker_share)
            if checker_share == "Send this to friends or post it on your timeline.":
                third_delay = random.randint(5, 6)
                time.sleep(third_delay)
                share_button.click()
                count= count+1
                time.sleep(one_sec_delay)
                driver.implicitly_wait(30)
                driver.find_element_by_xpath("//span[contains(text(),'Share now (Friends)')]").click()
                time.sleep(one_sec_delay)
            else:
              pass
        time.sleep(one_sec_delay)
    except Exception as e:
        print(e)
    print("Count =" + str(count))
    if count ==5:
        break
    scroll_height = driver.execute_script("return document.body.scrollHeight;")
    if (screen_height) * i > scroll_height:
        time.sleep(first_delay)
        continue




# body.send_keys(Keys.ARROW_DOWN)
# driver.find_element_by_xpath("//body[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/div[1]/div[4]/div[1]/div[4]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[4]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]").click()
# driver.find_element_by_xpath("//body[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]").click()
# body = driver.find_element_by_tag_name('body')
# # body.send_keys(Keys.DOWN)
# driver.find_element_by_xpath("//body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[4]/div[1]/span[1]/div[1]/div[1]").click()
# time.sleep(third_delay)
# driver.find_element_by_xpath("//span[contains(text(),'Log Out')]").click()
