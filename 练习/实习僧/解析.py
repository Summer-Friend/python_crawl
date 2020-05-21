'''
@Author: your name
@Date: 2020-03-07 19:31:47
@LastEditTime: 2020-03-08 10:13:52
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \vscode_code\练习\实习僧\解析.py
'''
from fontTools.ttLib import TTFont

def get_font():
    font = TTFont(r'E:\vscode_code\练习\实习僧\file.woff')
    font.saveXML(r'E:\vscode_code\练习\实习僧\file.xml')
    font_names = font.getGlyphOrder()
    ccmap = font['cmap'].getBestCmap()
    newmap = {}
    # 这些文字就是在FontEditor软件打开字体文件后看到的文字名字
    texts = ['','','1','3','7','9','6','8','2','4','5','0']
    font_name = {}
    # 将字体名字和它们所对应的乱码构成一个字典 
    for key ,value in ccmap.items():
        #转换成十六进制
        key = hex(key)
        value = value.replace('uni', '')
        a = 'u' + '0' * (4-len(value))+value
        newmap[key] = a
        
    #删除第一个没用的元素
    newmap.pop('0x78')
    #加上前缀变成Unicode
    for i, j in newmap.items():
        newmap[i] = eval("u"+"\'\\"+j+"\'")
    newdict = {}
    #根据网页上显示的字符样式改变键值对的显示
    for key, value in newmap.items():
        key_ = key.replace('0x', '&#x')
        newdict[key_] = value
    return newdict

mapping = {'&#xe028': 'k', '&#xe033': 'u', '&#xe063': '个', '&#xe077': 'n', '&#xe0f2': 'l', '&#xe11c': 'K', '&#xe1a2': 'p', '&#xe1c8': 'Q', '&#xe1f1': 'Z', '&#xe21c': '三', '&#xe24e': 'G', '&#xe2b9': 'g', '&#xe2d9': 'Y', '&#xe2e9': '软', '&#xe33e': 'P', '&#xe3c0': '天', '&#xe3f5': 'w', '&#xe430': 'o', '&#xe4f4': 'W', '&#xe4fe': 'U', '&#xe50e': '告', '&#xe51d': '广', '&#xe536': 'F', '&#xe5c6': '联', '&#xe5f3': 's', '&#xe62d': 'c', '&#xe63c': 'v', '&#xe64f': '0', '&#xe665': 'm', '&#xe6ce': 'i', '&#xe6e3': 'I', '&#xe749': '一', '&#xe795': '程', '&#xe7a8': 'q', '&#xe7be': '3', '&#xe7d6': 'E', '&#xe7f9': 't', '&#xe7fb': '4', '&#xe809': '端', '&#xe831': '银', '&#xe884': 'y', '&#xe893': '5', '&#xe8e6': '计', '&#xe95e': 'B', '&#xe96c': 'M', '&#xe975': '7', '&#xe976': 'b', '&#xe989': '二', '&#xe9be': '周', '&#xea2a': 'O', '&#xea94': '人', '&#xeabd': '财', '&#xeb61': '互', '&#xeb9c': 'X', '&#xebe2': '件', '&#xec15': '8', '&#xec2b': 'V', '&#xecaa': '工', '&#xed3c': 'h', '&#xed71': '行', '&#xed76': 'N', '&#xedf7': 'H', '&#xedfa': '场', '&#xee20': '年', '&#xee24': '市', '&#xee9e': '生', '&#xeed3': 'A', '&#xeee9': 'T', '&#xef13': 'z', '&#xef40': 'x', '&#xef43': 'S', '&#xef79': 'a', '&#xefcf': '网', '&#xf09c': '月', '&#xf154': '五', '&#xf221': '6', '&#xf242': '2', '&#xf3ff': 'r', '&#xf40a': '前', '&#xf434': '聘', '&#xf447': 'D', '&#xf475': '招', '&#xf485': '9', '&#xf48a': '政', '&#xf4a0': 'e', '&#xf58e': '师', '&#xf5e8': '四', '&#xf5f6': 'L', '&#xf6b4': 'f', '&#xf6d6': 'j', '&#xf6e5': '设', '&#xf718': '1', '&#xf71b': '会', '&#xf740': '作', '&#xf74d': 'd', '&#xf7c2': 'J', '&#xf7ef': 'R', '&#xf8b9': 'C'} # 映射字典，使用时需自行更新



def decrypt_text(text):
    # 定义文本信息处理函数，通过字典mapping中的映射关系解密
    for key, value in mapping.items():
        if key in text:
            text = text.replace(key, value)
        else:
            pass
    return text

'''
    for index,value in enumerate(texts):
        #把映射关系写成一个字典
        a = font_names[index].replace('uni', '&#x').lower() + ";"
        font_name[a] = value

    return font_name


font1 = TTFont(r'E:\vscode_code\练习\实习僧\file.woff')  # 打开本地字体文件01.ttf
uni_list = font1.getGlyphOrder()[2:]  # 前两个不算
print(uni_list)
print(get_font())
'''
a = '技术运维(\uede3\ue5ca\uede3\ue5ca春\ued08)'
print(get_font())
print(decrypt_text(a))