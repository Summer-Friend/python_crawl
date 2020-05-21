'''
@Author: your name
@Date: 2020-01-30 13:42:11
@LastEditTime : 2020-01-30 14:03:41
@LastEditors  : Please set LastEditors
@Description: In User Settings Edit
@FilePath: \vscode_code\爬虫测试\前程无忧\test.py
'''
import requests
from bs4 import BeautifulSoup
from pyecharts import Bar

ALL_DATA = []
def send_parse_urls(start_urls):
    headers = {
    "User-Agent": "Mozilla/5.0 (compatible; YandexBot/3.0; +http://yandex.com/bots)"
    }
    for start_url in start_urls:
        response = requests.get(start_url,headers=headers)
        # 编码问题的解决
        response = response.text.encode("raw_unicode_escape").decode("utf-8")
        soup = BeautifulSoup(response,'html.parser') #lxml解析器：性能比较好，html5lib：适合页面结构比较混乱的
        div_tatall = soup.find("div",class_="conMidtab") #find() 找符合要求的第一个元素
        tables = div_tatall.find_all("table") #find_all() 找到符合要求的所有元素的列表
        for table in tables:
            trs = table.find_all("tr")
            info_trs = trs[2:]
            for index,info_tr in enumerate(info_trs): # 枚举函数，可以获得索引
                # print(index,info_tr)
                # print("="*30)
                city_td = info_tr.find_all("td")[0]
                temp_td = info_tr.find_all("td")[6]
                # if的判断的index的特殊情况应该在一般情况的后面，把之前的数据覆盖
                if index==0:
                    city_td = info_tr.find_all("td")[1]
                    temp_td = info_tr.find_all("td")[7]
                city=list(city_td.stripped_strings)[0]
                temp=list(temp_td.stripped_strings)[0]
                ALL_DATA.append({"city":city,"temp":temp})
    return ALL_DATA

def get_start_urls():
    start_urls = [
       "http://www.weather.com.cn/textFC/hb.shtml",
        "http://www.weather.com.cn/textFC/db.shtml",
        "http://www.weather.com.cn/textFC/hd.shtml",
        "http://www.weather.com.cn/textFC/hz.shtml",
        "http://www.weather.com.cn/textFC/hn.shtml",
        "http://www.weather.com.cn/textFC/xb.shtml",
        "http://www.weather.com.cn/textFC/xn.shtml",
        "http://www.weather.com.cn/textFC/gat.shtml",
    ]
    return start_urls

def main():
    """
    主程序逻辑
    展示全国实时温度最低的十个城市气温排行榜的柱状图
    """
    # 1 获取所有起始url
    start_urls = get_start_urls()
    # 2 发送请求获取响应、解析页面
    data = send_parse_urls(start_urls)
    # print(data)
    # 4 数据可视化
        #1排序
    data.sort(key=lambda data:int(data["temp"]))
        #2切片，选择出温度最低的十个城市和温度值
    show_data = data[:10]
        #3分出城市和温度
    city = list(map(lambda data:data["city"],show_data))
    temp = list(map(lambda data:int(data["temp"]),show_data))
        #4创建柱状图、生成目标图
    chart = Bar("中国最低气温排行榜") #需要安装pyechart模块
    chart.add("",city,temp)
    chart.render("tempture.html")

if __name__ == '__main__':
    main()                                                                                                  