import requests
import re
import urllib.request, urllib.error
from bs4 import BeautifulSoup


find_image = re.compile(r'<img.*data-original="(.*?)"', re.S)  # 图片



def ask_url(url):
    head = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36"
    }
    #  伪装成浏览器
    request = urllib.request.Request(url, headers=head)
    html = ''
    try:
        response = urllib.request.urlopen(request)
        html = response.read().decode('utf-8')
    except urllib.error.URLError as e:
        if hasattr(e, 'code'):
            print(e.code)
        if hasattr(e, 'reason'):
            print(e.reason)
    return html


if __name__ == '__main__':
    head = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36"
    }

    datalist = []
    num = int(input("请输入要爬取的页数："))
    page = num + 1
    for i in range(1, page):
        url = 'https://fabiaoqing.com/biaoqing/lists/page/{}.html'.format(i)
        html = ask_url(url)
        soup = BeautifulSoup(html, 'html.parser')
    # print(soup)
        for item in soup.find_all('div', class_='tagbqppdiv'):

            item = str(item)
            # print(item)
            try:
                image = re.findall(find_image, item)[0]
            except:
                print("没有数据")
            # data.append(image)

            datalist.append(image)
    # print(datalist)
    n = 0
    for image_url in datalist:
        n = n + 1
        # 重新发起图片请求
        res = requests.get(url=image_url, headers=head)
        # res中已经有图片数据---二进制数据
        # 使用Python的open()函数进行存储
        with open('%d.jpg' % n, 'wb') as f:
            f.write(res.content)





