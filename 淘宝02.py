from selenium import webdriver
import time
import csv
import re


def search_product(key):

    driver.find_element_by_id('q').send_keys(key)
    driver.find_element_by_class_name("btn-search").click()
    driver.maximize_window()
    time.sleep(15)

    page = driver.find_element_by_xpath('//*[@id="mainsrp-pager"]/div/div/div/div[1]').text  # 找到页数标签
    page = re.findall(r'(\d+)', page)[0]
    return int(page)


def get_product():

    divs = driver.find_elements_by_xpath('//div[@class="items"]/div[@class="item J_MouserOnverReq  "]')
    for div in divs:
        info = div.find_element_by_xpath('.//div[@class="row row-2 title"]/a').text  # 商品名称
        price = div.find_element_by_xpath('.//div[@class="price g_price g_price-highlight"]/strong').text + '元'  # 价格
        deal = div.find_element_by_xpath('.//div[@class="deal-cnt"]').text  # 购买人数
        shop_name = div.find_element_by_xpath('.//div[@class="shop"]/a').text  # 店铺名称
        print(info, price, deal, shop_name, sep='|')
        with open('data2.csv', 'a', newline='') as file_csv:
            csv_writer = csv.writer(file_csv, delimiter=",")
            csv_writer.writerow([info, price, deal, shop_name])


def main():
    print('正在爬取第一页的数据')
    page = search_product(keywords)
    get_product()

    page_num = 1

    while page_num != page:
        print('*' * 100)
        print('正在爬取第{}页的数据'.format(page_num + 1))
        print('*' * 100)
        driver.get('https://s.taobao.com/search?q={}&s={}'.format(keywords, page_num*44))
        driver.implicitly_wait(2)
        driver.maximize_window()
        get_product()

        page_num += 1



if __name__ == '__main__':
    keywords = input("请输入你要搜索的商品关键字：")
    driver = webdriver.Chrome()
    driver.get('https://www.taobao.com')
    main()