import requests
from bs4 import BeautifulSoup


def get_city_aqi(city_pingyin):
    url = 'http://pm25.in' + city_pingyin
    url_text = requests.get(url).text

    soup = BeautifulSoup(url_text, 'html.parser')
    div_list = soup.find_all("div", {'class': 'span1'})  # 当前城市所有的污染物的值 8

    city_aqi = []

    for i in range(8):
        div_content = div_list[i]
        caption = div_content.find('div', {'class': 'caption'}).text.strip()  # 标题
        value = div_content.find('div', {'class': 'value'}).text.strip()  # value
        city_aqi.append((caption, value))
    return city_aqi


def get_all_cities():
    url = 'http://pm25.in/'
    city_list = []
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')

    city_div = soup.find_all('div', {'class': 'bottom'})[1]  # 全部城市的div
    city_link_list = city_div.find_all('a')  # 所有的城市的a
    for city_link in city_link_list:
        city_name = city_link.text  # 城市的名字
        city_pingyin = city_link['href']  # 城市的拼音
        city_list.append((city_name, city_pingyin))
        print(city_name)
    # print(city_list)
    return city_list


def main():
    city_list = get_all_cities()
    # print(city_list)
    result = []
    for city in city_list:
        city_name = city[0]
        city_pingyin = city[1]

        city_aqi = get_city_aqi(city_pingyin)
        # print(city_aqi)
        result.append((city_name, city_aqi))
        print('当前城市是{0}，污染物是{1}'.format(city_name, city_aqi))
    result = sorted(result, key = lambda k: k[1][0][1])
    print(result)


if __name__ == '__main__':
    main()
    # get_all_cities()
