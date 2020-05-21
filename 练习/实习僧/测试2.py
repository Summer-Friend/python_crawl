'''
@Author: your name
@Date: 2020-03-08 10:28:56
@LastEditTime: 2020-03-08 13:07:42
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \vscode_code\练习\实习僧\测试2.py
'''
from fontTools.ttLib import TTFont


mapping = {'&#xe028': 'k', '&#xe033': 'u', '&#xe063': '个', '&#xe077': 'n', '&#xe0f2': 'l', '&#xe11c': 'K', '&#xe1a2': 'p', '&#xe1c8': 'Q', '&#xe1f1': 'Z', '&#xe21c': '三', '&#xe24e': 'G', '&#xe2b9': 'g', '&#xe2d9': 'Y', '&#xe2e9': '软', '&#xe33e': 'P', '&#xe3c0': '天', '&#xe3f5': 'w', '&#xe430': 'o', '&#xe4f4': 'W', '&#xe4fe': 'U', '&#xe50e': '告', '&#xe51d': '广', '&#xe536': 'F', '&#xe5c6': '联', '&#xe5f3': 's', '&#xe62d': 'c', '&#xe63c': 'v', '&#xe64f': '0', '&#xe665': 'm', '&#xe6ce': 'i', '&#xe6e3': 'I', '&#xe749': '一', '&#xe795': '程', '&#xe7a8': 'q', '&#xe7be': '3', '&#xe7d6': 'E', '&#xe7f9': 't', '&#xe7fb': '4', '&#xe809': '端', '&#xe831': '银', '&#xe884': 'y', '&#xe893': '5', '&#xe8e6': '计', '&#xe95e': 'B', '&#xe96c': 'M', '&#xe975': '7', '&#xe976': 'b', '&#xe989': '二', '&#xe9be': '周', '&#xea2a': 'O', '&#xea94': '人', '&#xeabd': '财', '&#xeb61': '互', '&#xeb9c': 'X', '&#xebe2': '件', '&#xec15': '8', '&#xec2b': 'V', '&#xecaa': '工', '&#xed3c': 'h', '&#xed71': '行', '&#xed76': 'N', '&#xedf7': 'H', '&#xedfa': '场', '&#xee20': '年', '&#xee24': '市', '&#xee9e': '生', '&#xeed3': 'A', '&#xeee9': 'T', '&#xef13': 'z', '&#xef40': 'x', '&#xef43': 'S', '&#xef79': 'a', '&#xefcf': '网', '&#xf09c': '月', '&#xf154': '五', '&#xf221': '6', '&#xf242': '2', '&#xf3ff': 'r', '&#xf40a': '前', '&#xf434': '聘', '&#xf447': 'D', '&#xf475': '招', '&#xf485': '9', '&#xf48a': '政', '&#xf4a0': 'e', '&#xf58e': '师', '&#xf5e8': '四', '&#xf5f6': 'L', '&#xf6b4': 'f', '&#xf6d6': 'j', '&#xf6e5': '设', '&#xf718': '1', '&#xf71b': '会', '&#xf740': '作', '&#xf74d': 'd', '&#xf7c2': 'J', '&#xf7ef': 'R', '&#xf8b9': 'C'} # 映射字典，使用时需自行更新

def decrypt_text(text):
    # 定义文本信息处理函数，通过字典mapping中的映射关系解密
    for key, value in mapping.items():
        text = text.replace(key, value)
    return text


texts = '技术运维(\uf242\ue64f\uf242\ue64f春\uf475)'
t1 = ['\ue322\ue5ca\ue5ca-\ue145\ue5ca\ue5ca/天', '\uede3\ue5ca\ue5ca-\uf029\ue5ca\ue5ca/天']
t2 = ['\uf40a\ue809\uecaa\ue795\uf58e', '技术运维(\uf242\ue64f\uf242\ue64f春\uf475)', '在线家教英语辅导老\uf58e']

print(t1)
#print(decrypt_text(t2))
print('\uf242'=='&#f242')
