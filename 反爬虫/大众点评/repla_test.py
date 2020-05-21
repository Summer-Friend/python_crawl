'''
@Author: your name
@Date: 2020-03-05 10:48:39
@LastEditTime: 2020-03-05 22:30:25
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \vscode_code\爬虫测试\反爬虫\大众点评\test.py
'''
#items = [('&#xe651;', '&#xe6c5;')]

#映射字典，一定要先爬一下看看爬出来的是什么
mapping = {'glyph00000;': '', 'x;': '', '&#xf01f;': '1', '&#xed9d;': '3', '&#xecdb;': '7','&#xf164;': '9', 
           '&#xe651;': '6', '&#xf69f;': '8', '&#xef84;': '2', '&#xf446;': '4', '&#xe6c5;': '5', '&#xe2f5;': '0'}

def decrypt_text(text):
    # 定义文本信息处理函数，通过字典mapping中的映射关系解密
    for key, value in mapping.items():
        text = text.replace(key, value)
    return text

#哪怕是一堆玩意儿，依旧可以用replace替换掉
text = '&#xe651;&#xf164;a'
print(decrypt_text(text))

