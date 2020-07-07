import time
from selenium import webdriver


def get_content():
    title = driver.find_element_by_xpath('//*[@id="wrapper"]/div[4]/div/div[2]/h1').text
    info = driver.find_element_by_xpath('//*[@id="content"]').text
    # print(title, '\n', info)
    content = ('*'*100 + '\n' + title + '\n' + '*'*100 + '\n' + info + '\n')
    driver.implicitly_wait(5)
    time.sleep(1)
    print(content)
    with open('斗破苍穹.txt', 'a') as f:
        f.write(content)






if __name__ == '__main__':
    # url = "http://www.xbiquge.la/7/7877/3595785.html"

    driver = webdriver.Chrome()
    # driver.get(url)
    # driver.implicitly_wait(1)
    # get_content()

    # for link in driver.find_elements_by_xpath('//*[@id="list"]/dl/dd[1]'):
    #     print(link.get_attribute('href'))
    #     a = link.get_attribute('href')
    #     print(a)

    page_num = 3595841
    while page_num != 3597409:
        print('*'*100)
        print('第{}章'.format(page_num-3595784))
        print('*' * 100)
        url = 'http://www.xbiquge.la/7/7877/{}.html'.format(page_num)
        driver.get(url)
        driver.implicitly_wait(5)
        get_content()

        page_num += 1
