from selenium import webdriver as wb
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.alert import Alert
import time
options = Options()
options.add_extension('./extension/postman.crx')

#웹 브라우저 실행
driver_path = ("./driver/chromedriver")
driver = wb.Chrome(executable_path=driver_path, chrome_options=options)

#해당 URL을 브라우저로 실행
url = 'chrome-extension://coohjcphdfgbiolnekdpbcijmhambjff/index.html'

driver.get(url)

input_search = driver.find_element_by_id('url')
input_search.send_keys('https://www.naver.com')
param = driver.find_element_by_id('request-method-selector')
param.send_keys("post")
input_search.send_keys(Keys.ENTER)
time.sleep(2)  #2초동안 멈춤    
# driver.back()
input_search.clear()
input_search.send_keys('https://www.daum.com')
#input_search.send_keys(Keys.ENTER)
