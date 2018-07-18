import requests
from bs4 import BeautifulSoup
import pymysql


def crawler(url, keyword):
    # conn = pymysql.connect(host = 'localhost', port = 3306, user = 'root', password = 'root', db = 'db201501060102',
    #                        charset = 'utf8')
    # cursor = conn.cursor()

    data = requests.get(url).content
    soup = BeautifulSoup(data, 'html.parser')
    titles = soup.find_all('a')
    info = []
    for title in titles:
        # print(title.text)

        result = title.text.find(keyword)
        if result != -1:
            text = title.text
            href = title['href']
            print(text, href)
            # cursor.execute("INSERT INTO data(title,url)VALUES('{0}','{1}');".format(text, href))
            # conn.commit()
            info.append((text, href))
    print(info)
    return info
    # cursor.close()
    # conn.close()


if __name__ == '__main__':
    url = 'http://www.163.com'
    key = '习近平'
    crawler(url, key)
