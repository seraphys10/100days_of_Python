from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


driver = webdriver.Chrome("./chromedriver")

driver.get("https://www.q-net.or.kr/totalSearch.do?gSite=Q&searchQuery=%B9%DF%BC%DB%B9%E8%C0%FC%B1%E2%BC%FA%BB%E7&totalQuery=%B9%DF%BC%DB%B9%E8%C0%FC%B1%E2%BC%FA%BB%E7&searchMenu=dts&searchSort=date&pageNum=1&resFlag=off&qryStr=&detailChk=off")
driver.implicitly_wait(3)
url_list = driver.find_elements_by_css_selector("li > strong > a")
print(url_list)

href_list = []
for url in url_list:
    href = url.get_attribute('href')
    driver.get(href)
    driver.find_element_by_css_selector("td > a").click()
