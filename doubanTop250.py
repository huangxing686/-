from bs4 import BeautifulSoup
import re
import urllib.request, urllib.error
import xlwt
import sqlite3

find_link = re.compile(r'<a href="(.*?)">')  # 链接
find_image = re.compile(r'<img.*src="(.*?)"', re.S)  # 图片
find_title = re.compile(r'<span class="title">(.*)</span>')  # 片名
find_rating = re.compile(r'<span class="rating_num" property="v:average">(.*)</span>')  # 评分
find_judge = re.compile(r'<span>(\d*)人评价</span>')  # 评价人数
find_inq = re.compile(r'<span class="inq">(.*)</span>')  # 概况
find_bd = re.compile(r'<p class="">(.*?)</p>', re.S)  # 相关


def main():
    base_url = 'https://movie.douban.com/top250?start='
    # 1.爬取网页
    datalist = get_data(base_url)
    save_path = "豆瓣.xls"
    db_path = '豆瓣.db'
    # 3.保存数据
    save_data(datalist, save_path)
    #  ask_url(base_url)


def get_data(base_url):

    datalist = []
    for i in range(0, 10):
        url = base_url + str(i*25)
        html = ask_url(url)
        # 2.逐一解析数据
        soup = BeautifulSoup(html, 'html.parser')
        for item in soup.find_all('div', class_='item'):
            data = []
            item = str(item)

            link = re.findall(find_link, item)[0]  # 影片链接
            image = re.findall(find_image, item)[0]
            title = re.findall(find_title, item)[0]
            rating = re.findall(find_rating, item)[0]
            judge = re.findall(find_judge, item)[0]
            inq = re.findall(find_inq, item)
            bd = re.findall(find_bd, item)[0]
            bd = re.sub('/', ' ', bd)
            bd = re.sub(r'<br >', ' ', bd)
            bd = bd.strip()
            data.append(link)
            data.append(image)
            data.append(title)
            data.append(rating)
            data.append(judge)
            if len(inq) != 0:
                data.append(inq[0])
            else:
                data.append('')
            data.append(bd)
            datalist.append(data)
    print(len(datalist))
    print(datalist)

    return datalist


def ask_url(url):
    head = {
        "User-Agent": "Mozilla/5.0(Windows NT 6.1;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 84.0.4147.89Safari / 537.36"
    }
    #  伪装成浏览器
    request = urllib.request.Request(url, headers=head)
    html = ''
    try:
        response = urllib.request.urlopen(request)
        html = response.read().decode('utf-8')
        # print(html)
    except urllib.error.URLError as e:
        if hasattr(e, 'code'):
            print(e.code)
        if hasattr(e, 'reason'):
            print(e.reason)
    return html


def save_data(datalist, save_path):
    book = xlwt.Workbook(encoding='utf8', style_compression=0)
    sheet = book.add_sheet('豆瓣电影top250', cell_overwrite_ok=True)
    col = ('影片链接', '图片链接', '影片名', '评分', '评价人数', '概况', '相关信息')
    for i in range(0, 7):
        sheet.write(0, i, col[i])
    for i in range(0, 250):
        print('第%d条' % (i+1))
        data = datalist[i]
        for j in range(0, 7):
            sheet.write(i+1, j, data[j])
    book.save(save_path)


def save_data2(datalist, db_path):
    init_db(db_path)
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    pass


def init_db(db_path):
    sql = '''
        create table movies250
        (id integer primary key autoincrement ,
        info_link message_text ,
        image_link message_text ,
        name varchar ,
        score numeric ,
        rated numeric ,
        inq message_text ,
        msg message_text 
        )
    '''
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c.execute(sql)
    conn.commit()
    conn.close()


if __name__ == '__main__':
    main()
    # init_db('movie_test.db')

