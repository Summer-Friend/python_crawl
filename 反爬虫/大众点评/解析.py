'''
@Author: your name
@Date: 2020-03-05 10:08:23
@LastEditTime: 2020-03-08 13:11:59
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \vscode_code\爬虫测试\反爬虫\大众点评\解析.py
'''
from fontTools.ttLib import TTFont

def get_font():
    font = TTFont(r'E:\vscode_code\爬虫测试\反爬虫\大众点评\new_online_base64.woff')
    font_names = font.getGlyphOrder()
    print(font_names)
    # 这些文字就是在FontEditor软件打开字体文件后看到的文字名字
    texts = ['','','1','3','7','9','6','8','2','4','5','0']
    font_name = {}
    # 将字体名字和它们所对应的乱码构成一个字典 
    
    for index,value in enumerate(texts):
        #把映射关系写成一个字典
        a = font_names[index].replace('uni', '&#x').lower() + ";"
        font_name[a] = value

    return font_name

font1 = TTFont(r'E:\vscode_code\爬虫测试\反爬虫\大众点评\new_online_base64.woff')  # 打开本地字体文件01.ttf
font2 = TTFont(r'E:\vscode_code\练习\实习僧\shixi.ttf')  # 打开本地字体文件01.ttf
font1.saveXML(r'E:\vscode_code\爬虫测试\反爬虫\大众点评\new_online_base64.xml')
uni_list = font2.getGlyphOrder()[2:]  # 前两个不算
print(uni_list)
print(get_font())


