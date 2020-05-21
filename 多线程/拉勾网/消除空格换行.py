'''
@Author: your name
@Date: 2020-03-17 11:39:26
@LastEditTime: 2020-03-17 11:49:30
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \vscode_code\多线程\拉勾网\test.py
'''
#下面两种方法都可以使用
list1 = ['\n   \n', '\n', '\n 浔阳江头夜送客，枫叶荻花秋瑟瑟。','\n   \n 主人下马客在船，举酒欲饮无管弦。\n\n', '醉不成欢惨将别，别时茫茫江浸月\n', '\n\n']


lists = [x.strip() for x in list1]
set = list(set(lists))
set.sort(key=lists.index)
set.remove('')
print(set)


s=[x.strip() for x in list1 if x.strip()!='']
print(s)