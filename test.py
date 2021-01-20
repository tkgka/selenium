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
input_search.clear()
input_search.send_keys('https://www.nate.com')
param = driver.find_element_by_id('request-method-selector')
param.send_keys("get")
driver.find_element_by_id('headers-keyvaleditor-actions-open').click()

arr = [["Host","www.nate.com"],["Accept","text/html, application/xhtml+xml, image/jxr, */*"],["Connection","Keep-Alive"],["Content-Length",18]]
for i in range(1,len(arr)+1):
    head = driver.find_element_by_xpath(f'//*[@id="headers-keyvaleditor"]/div[{i}]/input[1]')
    val =  driver.find_element_by_xpath(f'//*[@id="headers-keyvaleditor"]/div[{i}]/input[2]')
    head.send_keys(arr[i-1][0])
    val.send_keys(arr[i-1][1])
#input_search.send_keys(Keys.ENTER)

# #2초동안 멈춤
# time.sleep(2)
# input_search.clear()    
# input_search.send_keys('https://www.naver.com')

# param.send_keys("post")
# driver.find_element_by_xpath('//*[@id="data-mode-selector"]/a[1]').click()
# #time.sleep(2)  #2초동안 멈춤    

# arr = [[1,2],[3,4],[5,6],[7,8],[9,10],[11,12],[13,14],[15,16]]
# print(len(arr))
# for i in range(1,len(arr)+1):
#     key = driver.find_element_by_xpath(f'//*[@id="formdata-keyvaleditor"]/div[{i}]/input[1]')
#     value = driver.find_element_by_xpath(f'//*[@id="formdata-keyvaleditor"]/div[{i}]/input[2]')
#     key.send_keys(arr[i-1][0])
#     value.send_keys(arr[i-1][1])
        

# input_search.send_keys(Keys.ENTER)
# for i in range(1,len(arr)+1):
#     driver.find_element_by_xpath(f'//*[@id="formdata-keyvaleditor"]/div[1]/a').click()


# param.send_keys("put")

# # insert to rows
# arr = [['ㄱ','ㄴ'],['ㄷ','ㄹ'],['ㅁ','ㅂ'],['ㅅ','ㅇ'],['ㅈ','ㅊ'],['ㅋ','ㅌ'],['ㅍ','ㅎ'],['ㅏ','ㅑ']]
# print(len(arr))
# for i in range(1,len(arr)+1):
#     key = driver.find_element_by_xpath(f'//*[@id="formdata-keyvaleditor"]/div[{i}]/input[1]')
#     value = driver.find_element_by_xpath(f'//*[@id="formdata-keyvaleditor"]/div[{i}]/input[2]')
#     key.send_keys(arr[i-1][0])
#     value.send_keys(arr[i-1][1])
# input_search.send_keys(Keys.ENTER)

# #delete rows
# for i in range(1,len(arr)+1):
#     driver.find_element_by_xpath(f'//*[@id="formdata-keyvaleditor"]/div[1]/a').click()


# # driver.back()


