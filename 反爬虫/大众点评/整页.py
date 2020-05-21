'''
@Author: your name
@Date: 2020-03-05 21:05:40
@LastEditTime: 2020-03-07 10:59:34
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \vscode_code\爬虫测试\反爬虫\大众点评\整页.py
'''
import requests
import re
from requests.exceptions import  RequestException


url = 'http://www.dianping.com/hangzhou/ch10/g110'

def get_one_page(url):
    try:
        headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}
        response = requests.get(url, headers = headers)
        if response.status_code==200:
            return response.text
        return None
    except RequestException:
        return None
#这个映射是猫眼的woff文件，就随便改了几个量让他刚好匹配罢了
mapping = {'glyph00000;': '', 'x;': '', '&#xf01f;': '1', '&#xe818;': '3', '&#xeccd;': '7','&#xf164;': '9', 
           '&#xe651;': '6', '&#xf1e9;': '8', '&#xea00;': '2', '&#xf446;': '4', '&#xe6c5;': '5', '&#xe2f5;': '0'}


def decrypt_text(text):
    # 定义文本信息处理函数，通过字典mapping中的映射关系解密
    for key, value in mapping.items():
        text = text.replace(key, value)
    return text


def parse_one_page(html):
    '''
    i=r'@font-face{font-family:myFont;src:url((.*?));}'      
    base64_code=re.findall(i,html.replace(' ',''))
    print(base64_code)
    '''
    pattern = re.compile(r'<div class="comment">.*<b>(.*?)<svgmtsi class="shopNum">(.*?)</svgmtsi>(.*?)</b>\n条点评',re.S)##正则
    #pattern = re.compile(r'<b>(.*?)<svgmtsi class="shopNum">(.*?)</svgmtsi>(.*?)</b>',re.S)##正则
    items = re.findall(pattern,html) 
    print(items)
  
    

def main():
    html = get_one_page(url)
    parse_one_page(html)

if __name__=='__main__':
    main()