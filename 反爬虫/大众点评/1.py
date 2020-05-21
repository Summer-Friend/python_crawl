'''
@Author: your name
@Date: 2020-03-04 19:21:21
@LastEditTime: 2020-03-05 21:18:59
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \vscode_code\爬虫测试\反爬虫\大众点评\1.py
'''
import re
import requests
#from scrapy import Selector
from fontTools.ttLib import TTFont
 
url = 'http://www.dianping.com/shop/131357182'

def get_one_page(url):
    try:
        headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}
        response = requests.get(url, headers = headers)
        if response.status_code==200:
            return response.text
        return None
    except RequestException:
        return None
    
def get_font():
    font = TTFont(r'E:\vscode_code\爬虫测试\反爬虫\大众点评\new_online_base64.woff')
    font_names = font.getGlyphOrder()
    
    # 这些文字就是在FontEditor软件打开字体文件后看到的文字名字
    texts = ['','','1','3','7','9','6','8','2','4','5','0']
    font_name = {}
    # 将字体名字和它们所对应的乱码构成一个字典 
    
    for index,value in enumerate(texts):
        a = font_names[index].replace('uni', '&#x').lower() + ";"
        font_name[a] = value

    return font_name

#映射字典，一定要先爬一下看看爬出来的是什么
#这个映射是猫眼的woff文件，就随便改了几个量让他刚好匹配罢了
mapping = {'glyph00000;': '', 'x;': '', '&#xe434;': '1', '&#xed9d;': '3', '&#xecdb;': '7','&#xf164;': '9', 
           '&#xe651;': '6', '&#xf69f;': '8', '&#xef84;': '2', '&#xf446;': '4', '&#xe6c5;': '5', '&#xe2f5;': '0'}


def decrypt_text(text):
    # 定义文本信息处理函数，通过字典mapping中的映射关系解密
    for key, value in mapping.items():
        text = text.replace(key, value)
    return text


def parse_one_page(html):
    
    pattern = re.compile(r'<span id="reviewCount" class="item"> <d class="num">(.*?)</d><d class="num">(.*?)</d> 条评论 </span>',re.S)##正则
    items = re.findall(pattern,html) 
    print(items)
    '''
    for item in items:
        item2 = [0]*len(item)
        for i in range(len(item)):
            item2[i] = decrypt_text(item[i])
            #print(item2[i])
        item_clean = ''.join(item2)
        print(item_clean)
    '''
    

def main():
    html = get_one_page(url)
    #print('打印第',(i+1),'页')
    parse_one_page(html)

if __name__=='__main__':
    main()