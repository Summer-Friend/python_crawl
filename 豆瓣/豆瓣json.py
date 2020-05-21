'''
@Author: your name
@Date: 2020-02-06 13:10:51
@LastEditTime : 2020-02-06 13:25:12
@LastEditors  : Please set LastEditors
@Description: In User Settings Edit
@FilePath: \vscode_code\爬虫测试\豆瓣.py\豆瓣json.py
'''
# 目标: https://movie.douban.com/explore#!type=movie&tag=%E7%83%AD%E9%97%A8&sort=recommend&page_limit=20&page_start=0
# 返回的是json数据，那么就不需要解析器了。直接转字典就好了。

import requests
import json

# 热门电视剧
def douban_tv(rowCount):
    url='https://movie.douban.com/j/search_subjects?type=tv&tag=%E7%83%AD%E9%97%A8&sort=recommend&page_limit='+rowCount+'&page_start=0'
    print(url)
    # 解决出现403拒绝访问
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                             'Chrome/51.0.2704.63 Safari/537.36'}
    # 使用request模块打开并获取网页内容
    response = requests.get(url, headers=headers, verify=False, timeout=30)   # 禁止重定向
    content = response.text
    print(content)
    # 返回的是json，那么就直接解码转为字典。不需要解析器bs了
    result = json.loads(content)
    tvs = result['subjects']

    tv_list = []        # 创建一个列表
    for i in range (0,len(tvs)):
        tv={}             # 创建一个字典
        tv['rate']=tvs[i]['rate']            # 评分
        tv['title']=tvs[i]['title']          # 电影名称
        tv['cover'] = tvs[i]['cover']  # 封面图片的地址
        tv['url'] = tvs[i]['url']  # 电影的豆瓣链接
        tv_list.append(tv)               # 列表存放字典
    return tv_list

# 热门电影
def douban_movie(rowCount):
    url='https://movie.douban.com/j/search_subjects?type=movie&tag=%E7%83%AD%E9%97%A8&sort=recommend&page_limit='+str(rowCount)+'&page_start=0'

    # 解决出现403拒绝访问
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                             'Chrome/51.0.2704.63 Safari/537.36'}
    # 使用request模块打开并获取网页内容
    response = requests.get(url,headers = headers,verify=False,timeout=30)
    print(response.text)   # 报错：json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)
                    # 解决：以后在使用json时，最好先输出一下参数，检查一下是否符合格式？
    content = response.content

    # json格式转为字典
    result = json.loads(content)
    print(content,result)

    # 获取相关信息并存入列表的字典中
    movie_list = []
    mos = result['subjects']
    for i in range (0,len(mos)):
        mo = {}
        mo['rate']=mos[i]['rate']
        mo['cover']=mos[i]['cover']
        mo['url']=mos[i]['url']
        mo['title']=mos[i]['title']
        movie_list.append(mo)       # 列表存放字典
    return movie_list

# 保存为csv文件
def output_csv(datalist):
    print(type(datalist),len(datalist))  # <class 'list'> 100
    import csv
    # 准备好存储的csv文件
    csv_file = open(r'E:\vscode_code\爬虫测试\豆瓣.py\douban_data.csv', 'w', newline='', encoding='utf-8-sig')  # 解决中文乱码问题
    writer = csv.writer(csv_file)
    writer.writerow(['评分', '作品名称', '豆瓣链接','封面图片'])
    for data in datalist:
        writer.writerow([data['rate'], data['title'],data['url'],data['cover']])
    csv_file.close()

if __name__=="__main__":
    category = 1         #input('请输入爬取的类别代号(电视剧：0，电影：1):')
    rowCount = 100       #input('请输入爬取的条数：')
    result = douban_movie(rowCount)
    """
    if category=='0':
        print('爬取电视剧中，请稍后...')
        result = douban_tv(rowCount)
    elif category=='1':
        print('爬取电影中，请稍后...')
        result = douban_movie(rowCount)
    else:
        print('输入错误，暂不支持，请重试...')
    """

   # 持久化保存
    # for i in result:
    #     print(i)
    output_csv(result)

    print("爬虫完毕，文件已生成。快去查看吧")
