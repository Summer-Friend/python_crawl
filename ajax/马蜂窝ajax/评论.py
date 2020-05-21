'''
@Author: your name
@Date: 2020-03-11 19:22:57
@LastEditTime: 2020-03-11 21:31:22
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \vscode_code\爬虫测试\马蜂窝ajax\crawl.py
'''
#https://blog.csdn.net/qq_45373920/article/details/104037607
import re
import time
import requests
#评论内容所在的url，？后面是get请求需要的参数内容
comment_url='http://pagelet.mafengwo.cn/poi/pagelet/poiCommentListApi?'

#refer里面才是正常的访问网址
requests_headers={
    'Referer': 'http://www.mafengwo.cn/poi/5426285.html',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'
}#请求头

for num in range(1,6):
    requests_data={
        'params': '{"poi_id":"5426285","page":"%d","just_comment":1}' % (num)   #经过测试只需要用params参数就能爬取内容
        }
    response =requests.get(url=comment_url,headers=requests_headers,params=requests_data)
    if 200==response.status_code:
        page = response.content.decode('unicode-escape', 'ignore').encode('utf-8', 'ignore').decode('utf-8')#爬取页面并且解码
        page = page.replace('\\/', '/')#将\/转换成/
        #日期列表
        date_pattern = r'<a class="btn-comment _j_comment" title="添加评论">评论</a>.*?\n.*?<span class="time">(.*?)</span>'
        date_list = re.compile(date_pattern).findall(page)
        #星级列表
        star_pattern = r'<span class="s-star s-star(\d)"></span>'
        star_list = re.compile(star_pattern).findall(page)
        #评论列表
        comment_pattern = r'<p class="rev-txt">([\s\S]*?)</p>'
        comment_list = re.compile(comment_pattern).findall(page)
        for num in range(0, len(date_list)):
            #日期
            date = date_list[num]
            #星级评分
            star = star_list[num]
            #评论内容，处理一些标签和符号
            comment = comment_list[num]
            comment = str(comment).replace('&nbsp;', '')
            comment = comment.replace('<br>', '')
            comment = comment.replace('<br />', '')
            print(date+"\t"+star+"\t"+comment)
    else:
        print("爬取失败")
