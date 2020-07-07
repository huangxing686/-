from selenium import webdriver
import time
import csv

def search_product(key):
    driver.find_element_by_id('q').send_keys(key)
    driver.find_element_by_class_name("btn-search").click()
    driver.maximize_window()
    time.sleep(5)


def get_product():
    divs = driver.find_elements_by_xpath('//div[@class="items"]/div[@class="item J_MouserOnverReq  "]')
    for div in divs:
        info = div.find_element_by_xpath('.//div[@class="row row-2 title"]/a').text  # 商品名称
        price = div.find_element_by_xpath('.//div[@class="price g_price g_price-highlight"]/strong').text + '元'  # 价格
        deal = div.find_element_by_xpath('.//div[@class="deal-cnt"]').text  # 购买人数
        shop_name = div.find_element_by_xpath('.//div[@class="shop"]/a').text  # 店铺名称
        print(info, price, deal, shop_name, sep='|')
        with open('data.csv', 'a', newline='') as file_csv:
            csv_writer = csv.writer(file_csv, delimiter=",")
            csv_writer.writerow([info, price, deal, shop_name])


def main():
    search_product(keywords)
    get_product()




if __name__ == '__main__':
    keywords = input("请输入你要搜索的商品关键字：")
    driver = webdriver.Chrome()
    driver.get('https://www.taobao.com')
    main()