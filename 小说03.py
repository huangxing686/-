import time
from selenium import webdriver
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='gb18030')


def get_content():
    title = driver.find_element_by_xpath('//*[@id="content"]/h2').text
    info = driver.find_element_by_xpath('//*[@id="content"]/p[2]').text
    # print(title, '\n', info)
    content = ('*'*100 + '\n' + title + '\n' + '*'*100 + '\n' + info + '\n')
    print(content)
    with open('破云.txt', 'a',encoding='utf-8') as f:
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

    page_num = 24898813
    while page_num != 25907345:
        print('*'*100)
        print('第{}章'.format(page_num-24898813))
        print('*' * 100)
        url = 'https://www.fpzw.com/xiaoshuo/108/108004/{}.html'.format(page_num)
        driver.get(url)
        driver.implicitly_wait(5)
        get_content()
        if page_num == 24898905:
            page_num = 24911995

        page_num += 1
