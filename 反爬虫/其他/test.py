'''
@Author: your name
@Date: 2020-03-05 16:30:52
@LastEditTime: 2020-03-05 17:18:48
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \vscode_code\爬虫测试\反爬虫\其他\test.py
'''
import requests,json,re
import xml.etree.ElementTree as et

response = requests.get('https://www.shixiseng.com/interns?page=10&keyword=%E6%95%B0%E6%8D%AE%E5%BA%93&type=intern&months=&days=&degree=&official=&enterprise=&salary=-0&publishTime=&sortType=&city=%E5%85%A8%E5%9B%BD&internExtend=',timeout=5)
i=r'@font-face{font-family:myFont;src:url((.*?));}'

base64_code=re.findall(i,response.text.replace(' ',''))#[0][0].replace('(','').replace(')','')


root = et.parse(r'E:\vscode_code\爬虫测试\反爬虫\其他\字体.xml').getroot()
map_ele = root.find('cmap').find('cmap_format_4').findall('map')
print(map_ele)
map_dict = {}
for index,value in enumerate(map_ele):
    print(index, value)
    
        #把映射关系写成一个字典
        a = map_dict[index].replace('uni', '&#x').lower() + ";"
        map_dict[a] = value
        
print(map_dict)
'''
# 把map那一堆数据存到字典中
for m in map_ele:
    code = m.attrib['code'].replace('0x', '')
    print(m.attrib['name'])
    print(m.attrib['code'])
'''       