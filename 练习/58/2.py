'''
@Author: your name
@Date: 2020-03-08 13:34:59
@LastEditTime: 2020-03-08 13:40:43
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \vscode_code\练习\58\2.py
'''
import re
import base64
import chardet
import requests
from scrapy import Selector
from fontTools.ttLib import TTFont

url = 'https://piaofang.maoyan.com/?ver=normal'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
}
response = requests.get(url=url, headers=headers).content  # 得到字节
charset = chardet.detect(response).get('encoding')  # 得到编码格式
response = response.decode(charset, "ignore")  # 解码得到字符串

# 第一次获取的字体，以及对应编码位置，需要手动写一次。
origin_fonts = TTFont(r'E:\vscode_code\练习\58\maoyan.woff')
origin_obj_list1 = origin_fonts.getGlyphNames()[1:-1]  # 获取所有字符的对象，去除第一个和最后一个,之前的图已经解释清楚为什么去掉最后一个和第一个。
origin_uni_list1 = origin_fonts.getGlyphOrder()[2:]  # 获取所有编码，去除前2个。
origin_dict = {'uniF855': '1', 'uniF755': '8', 'uniF617': '9', 'uniE4CA': '4', 'uniE912': '6', 'uniF514': '3',
               'uniE3A5': '7', 'uniF594': '5', 'uniF16A': '0', 'uniF09C': '2'}  # 写出第一次字体文件的编码和对应字体。

# 获取字体文件的base64编码
online_ttf_base64 = re.findall(r"base64,(.*)\) format", response)[0]
online_base64_info = base64.b64decode(online_ttf_base64)
with open(r'E:\vscode_code\练习\58\online_base64.ttf', 'wb')as f:
    f.write(online_base64_info)
online_base64_fonts = TTFont(r'E:\vscode_code\练习\58\online_base64.ttf')  # 网上动态下载的字体文件。
online_obj_list2 = online_base64_fonts.getGlyphNames()[1:-1]  # 同上。
online_uni_list2 = online_base64_fonts.getGlyphOrder()[2:]

for uni2 in online_uni_list2:
    obj2 = online_base64_fonts['glyf'][uni2]  # 获取编码uni2在online_base64.ttf中对应的对象
    for uni1 in origin_uni_list1:
        obj1 = origin_fonts['glyf'][uni1]  # 获取编码uni1在origin.ttf 中对应的对象。
        if obj1 == obj2:  # 如果对象一等于对象二
            dd = "&#x" + uni2[3:].lower() + ';'  # 把编码uni2替换成Unicode编码格式。
            if dd in response:  # 如果编码uni2的Unicode编码格式在response中，那么替换成origin_dict[uni1]的字体。
                response = response.replace(dd, origin_dict[uni1])
response_info = Selector(text=response)
all_info = response_info.xpath('//ul[@class="canTouch"]')  # 获取所有的信息
print('电影名字' + '\t' + '实时票房(万元)' + '\t' + '票房占比' + '\t' + '排片占比' + '\t' + '上座率')
for each_info in all_info:
    movie_name = each_info.xpath('li[1]/b/text()').extract_first()  # 电影名字
    ticket_number = each_info.xpath('li[2]/b/i[@class="cs"]/text()').extract_first()  # 实时票房(万元)
    ticket_rate = each_info.xpath('li[3]/i[@class="cs"]/text()').extract_first()  # 票房占比
    film_rate = each_info.xpath('li[4]/i[@class="cs"]/text()').extract_first()  # 排片占比
    upper_seat_rate = each_info.xpath('li[5]/span/i[@class="cs"]/text()').extract_first()  # 上座率
    print(movie_name + '\t' + ticket_number + '\t' + ticket_rate + '\t' + film_rate + '\t' + upper_seat_rate)
