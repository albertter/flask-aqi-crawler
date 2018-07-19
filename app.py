from flask import Flask, request, render_template, redirect
from crawler import crawler
from aqi import get_city_aqi
from aqi import get_all_cities

app = Flask(__name__)


@app.route('/aqi', methods = ['POST', 'GET'])
def aqi():
    result = []
    city_list = get_all_cities()
    for city in city_list:
        city_name = city[0]
        city_pingyin = city[1]
        city_aqi = get_city_aqi(city_pingyin)
        if city_aqi[0][1] != 0:
            result.append((city_name, city_aqi))
        print('当前城市是{0}，污染物是{1}'.format(city_name, city_aqi))

    pollutant_no = 0
    num = 10
    if request.method == 'POST':
        num = request.form['num']
        num = int(num)
        pollutant = request.form['pollutant']
        pollutant_no = int(pollutant)

    result.sort(key = lambda k: k[1][pollutant_no][1])

    return render_template('aqi.html', result = result, num = num)


@app.route('/', methods = ['GET', 'POST'])
def hello_world():
    result = []
    keyword = ''
    if request.method == 'POST':
        url = request.form['url']
        keyword = request.form['keyword']
        result = crawler(url, keyword)

    return render_template('index.html', result = result, keyword = keyword)


if __name__ == '__main__':
    app.run(debug = True)
