'''
@Author: your name
@Date: 2020-03-11 20:49:20
@LastEditTime: 2020-03-11 21:46:28
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \vscode_code\爬虫测试\ajax\豆瓣\1.py
'''
#这个和json动态加载时类似的，但是这个可以利用json也可以利用ajax的param参数进行抓取
import requests
import time
from fake_useragent import UserAgent


class DoubanSpider(object):
    def __init__(self):
        self.base_url = 'https://movie.douban.com/j/chart/top_list?'
        self.i = 0

    def get_html(self, params):
        headers = {'User-Agent': UserAgent().random}
        #因为有了param参数让他得以定位
        res = requests.get(url=self.base_url, params=params, headers=headers)
        res.encoding = 'utf-8'
        html = res.json()  # 将json格式的字符串转为python数据类型
        self.parse_html(html)  # 直接调用解析函数

    def parse_html(self, html):
        # html: [{电影1信息},{电影2信息},{}]
        item = {}
        for one in html:
            item['name'] = one['title']  # 电影名
            item['score'] = one['score']  # 评分
            item['time'] = one['release_date']  # 打印测试
            # 打印显示
            print(item)
            self.i += 1

    # 获取电影总数
    def get_total(self, typ):
        # 异步动态加载的数据 都可以在XHR数据抓包
        url = 'https://movie.douban.com/j/chart/top_list_count?type={}&interval_id=100%3A90'.format(typ)
        ua = UserAgent()
        html = requests.get(url=url, headers={'User-Agent': ua.random}).json()
        total = html['total']

        return total

    def main(self):
        typ = '剧情'
        typ_dict = {'剧情': '11', '喜剧': '24', '动作': '5'}
        typ = typ_dict[typ]
        total = self.get_total(typ)  # 获取该类型电影总数量

        for page in range(0, int(total), 20):
            params = {
                'type': typ,
                'interval_id': '100:90',
                'action': '',
                'start': str(page),
                'limit': '20'}
            self.get_html(params)
            time.sleep(1)
        print('爬取的电影的数量:', self.i)


if __name__ == '__main__':
    spider = DoubanSpider()
    spider.main()