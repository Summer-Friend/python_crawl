'''
@Author: your name
@Date: 2020-03-08 10:33:02
@LastEditTime: 2020-03-08 13:29:14
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \vscode_code\练习\58\1.py
'''
import requests
import re
from fontTools.ttLib import TTFont

url = 'https://maoyan.com/'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36',
}

session = requests.session()
response = session.get(url,headers=headers)

def get_woff_file():
    file_url = re.search("src:.*?,.*?url\('(.*?)'\) format\('woff'\);",response.text,re.S).group(1)
    print(file_url)
    with open(r'E:\vscode_code\练习\58\maoyan.woff','wb') as fp:
        content = session.get('http:' + file_url, headers=headers).content
        fp.write(content)

def parse_font():
    font = TTFont(r'E:\vscode_code\练习\58\maoyan.woff')
    font.saveXML(r'E:\vscode_code\练习\58\maoyan.xml')
    font_base_order = font.getGlyphOrder()[2:]
    print(font_base_order)
    # 根据第一次下载的文件写出对应
    map_list = ['1','2','8','0','7','6','3','5','9','4']

    font_new = TTFont(r'E:\vscode_code\练习\58\maoyan.woff')
    font_new.saveXML(r'E:\vscode_code\练习\58\maoyan.xml')
    font_new_order = font_new.getGlyphOrder()[2:]
    print(font_new_order)

    base_flag_list = list()
    new_flag_list = list()
    # 得到两个二维列表，对里面没个一维列表进行内容的比对，得到对应的字体
    for i,j in zip(font_base_order,font_new_order):
        flag_base = font['glyf'][i].flags
        flag_new = font_new['glyf'][j].flags
        base_flag_list.append(list(flag_base))
        new_flag_list.append(list(flag_new))

    memory_dict = dict()
    for index1,x in enumerate(base_flag_list):
        for index2,y in enumerate(new_flag_list):
            if common(x,y):
                key = font_new_order[index2]
                key = '&#x' + key.replace('uni','').lower() + ';'
                memory_dict[key] = map_list[index1]
    print(memory_dict)
    return memory_dict

def get_data(memory_dict):
    name = re.findall('<span class="ranking-top-moive-name">(.*?)</span>', response.text, re.S)
    all_data = re.findall('<span class="stonefont">(.*?)</span>万', response.text, re.S)
    print(name)
    print(all_data)
    for data in all_data:
        for key,value in memory_dict.items():
            data = data.replace(key,value)
        print(data)# 只是做测试用就不提取那么多东西了

def common(list1,list2):
    len1 = len(list1)
    len2 = len(list2)
    if len1 != len2:
        return False
    for i in range(len1):
        if list1[i] != list2[i]:
            return False
    return True

if __name__ == '__main__':
    get_woff_file()
    memory_dict = parse_font()
    get_data(memory_dict)
