from selenium import webdriver
import time
import csv

def search_product(key):
    driver.find_element_by_id('wd').send_keys(key)
    driver.find_element_by_id('sss').click()
    driver.maximize_window()
    # driver.implicitly_wait(5)
    driver.find_element_by_xpath('//*[@id="checkform"]/table/tbody/tr[2]/td[1]/a').click()
    # title = driver.find_element_by_xpath('//*[@id="list"]/dl/dd[1]/a').text
    # #driver.implicitly_wait(5)
    # # info = driver.find_element_by_xpath('//*[@id="content"]').text
    # print(title)






def main():
    search_product(keywords)





if __name__ == '__main__':
    keywords = input("请输入你要搜索的小说关键字：")
    driver = webdriver.Chrome()
    driver.get('http://www.xbiquge.la/')
    main()