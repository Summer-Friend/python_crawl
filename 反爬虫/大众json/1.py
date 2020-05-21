'''
@Author: your name
@Date: 2020-03-06 08:43:24
@LastEditTime: 2020-03-10 17:39:20
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \vscode_code\爬虫测试\反爬虫\大众json\1.py
'''
"""
list_city :城市的ID号码，依次是：上海，北京，广州，深圳，天津，杭州，南京，苏州，成都，武汉，重庆，西安
"""
import json
import random
import requests
import pandas as pd 
import csv 

csv_file = open(r'E:\vscode_code\爬虫测试\反爬虫\大众json\大众_data.csv', 'w', newline='', encoding='utf-8-sig')  # 解决中文乱码问题
writer = csv.writer(csv_file)
writer.writerow(['城市地址', '商铺网址', '商铺名称', '商品编号', '商铺星级',  '所在区域名称', 
                 '分类名称', '口味评分', '环境评分', '服务评分','人均消费'])

# 城市列表
list_city = [["上海","fce2e3a36450422b7fad3f2b90370efd71862f838d1255ea693b953b1d49c7c0"],["北京","d5036cf54fcb57e9dceb9fefe3917fff71862f838d1255ea693b953b1d49c7c0"],["广州","e749e3e04032ee6b165fbea6fe2dafab71862f838d1255ea693b953b1d49c7c0"],["深圳","e049aa251858f43d095fc4c61d62a9ec71862f838d1255ea693b953b1d49c7c0"],["天津","2e5d0080237ff3c8f5b5d3f315c7c4a508e25c702ab1b810071e8e2c39502be1"],["杭州","91621282e559e9fc9c5b3e816cb1619c71862f838d1255ea693b953b1d49c7c0"],["南京","d6339a01dbd98141f8e684e1ad8af5c871862f838d1255ea693b953b1d49c7c0"],["苏州","536e0e568df850d1e6ba74b0cf72e19771862f838d1255ea693b953b1d49c7c0"],["成都","c950bc35ad04316c76e89bf2dc86bfe071862f838d1255ea693b953b1d49c7c0"],["武汉","d96a24c312ed7b96fcc0cedd6c08f68c08e25c702ab1b810071e8e2c39502be1"],["重庆","6229984ceb373efb8fd1beec7eb4dcfd71862f838d1255ea693b953b1d49c7c0"],["西安","ad66274c7f5f8d27ffd7f6b39ec447b608e25c702ab1b810071e8e2c39502be1"]]
# 请求头
USER_AGENT_LIST = [
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
    "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5"]

#random使得被抽取的元素作为一个片断返回，但是是以列表形式带有中括号所以要加[0]
head = {
'User-Agent': '{0}'.format(random.sample(USER_AGENT_LIST, 1)[0])  # 随机获取
}

flag = 0
code = 0
#shop_list = []
# 解析
def findFood(city,data):
    global flag,code
    for data in json.loads(data)["shopBeans"]:
        #print(data["shopPower"])
        shop_list = []
        shop  ={}
        flag +=1
        #城市地址
        shop['city'] = city
        # 人均消费
        shop['avgPrice'] = data["avgPrice"]
        # 分类名称
        shop['mainCategoryName'] = data["mainCategoryName"]
        # 所在区域名称
        shop['mainRegionName'] = data["mainRegionName"]
        # 口味评分
        shop['tasteScore'] = data["refinedScore1"]
        # 环境评分
        shop['environmentScore'] = data["refinedScore2"]
        # 服务评分
        shop['serviceScore'] = data["refinedScore3"]
        # 商品编号
        shop['shopId'] = data["shopId"]
        # 商铺网址
        shop['shopUrl'] = "http://www.dianping.com/shop/"+data["shopId"]
        # 商铺名称
        shop['shopName'] = data["shopName"]
        # 商铺星级
        shop['shopPower'] = data["shopPower"]
        
        shop_list.append(shop)
        # 准备好存储的csv文件
        csv_file = open(r'E:\vscode_code\爬虫测试\反爬虫\大众json\大众_data.csv', 'a+', newline='', encoding='utf-8-sig')  # 解决中文乱码问题
        writer = csv.writer(csv_file)
        #writer.writerow(['市', '省', '价值'])
        for data in shop_list:
            writer.writerow([data['city'], data['shopUrl'],data['shopName'], data['shopId'], data['shopPower'],
                            data['mainRegionName'], data['mainCategoryName'], data['tasteScore'], 
                            data['environmentScore'], data['serviceScore'], data['avgPrice']])
        csv_file.close()
        
    print("总条数：", flag)


# 抓取
def foodSpider(city_list):
    city = city_list[0]
    url = city_list[1]
    base_url = "http://www.dianping.com/mylist/ajax/shoprank?rankId="+url
    html = requests.get(base_url, headers=head)
    findFood(city=city, data=str(html.text))


if __name__ == '__main__':
    #foodSpider(list_city[0])
    
    for city_data in list_city:
        foodSpider(city_data)
    