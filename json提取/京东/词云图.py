'''
@Author: your name
@Date: 2020-03-04 08:44:58
@LastEditTime: 2020-03-04 11:30:12
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \vscode_code\爬虫测试\json提取\京东\ciyun.py
'''

#https://www.cnblogs.com/delav/p/7845539.html
import jieba
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import matplotlib.pyplot as plt
from PIL import Image

#蒙版的背景图
mask = plt.imread(r'E:\vscode_code\vscode_python_test\数据可视化\jiaba\20190131160157591.jpg')

wc = WordCloud(background_color='white',  # 背景颜色,什么yellow啥的也行
               max_words=1000,  # 最大词数
               mask=mask,  # 以该参数值作图绘制词云，这个参数不为空时，width和height会被忽略
               max_font_size=100,  # 显示字体的最大值
               stopwords=STOPWORDS.add('苟利国'),  # 使用内置的屏蔽词，再添加'苟利国'
               random_state=42,  # 为每个词返回一个PIL颜色
               # width=1000,  # 图片的宽
               # height=860  #图片的长
               )
# WordCloud各含义参数请点击 wordcloud参数

# 添加自己的词库分词，比如添加'金三胖'到jieba词库后，当你处理的文本中含有金三胖这个词，
# 就会直接将'金三胖'当作一个词，而不会得到'金三'或'三胖'这样的词
jieba.add_word('金三胖')

# 打开词源的文本文件
#encoding="ANSI"是记事本的编码方式可加可不加
text = open(r'E:\vscode_code\爬虫测试\json提取\京东\comm.txt', 'r', encoding="ANSI").read()


# 该函数的作用就是把屏蔽词去掉，使用这个函数就不用在WordCloud参数中添加stopwords参数了
# 把你需要屏蔽的词全部放入一个stopwords文本文件里即可
def stop_words(texts):
    words_list = []
    word_generator = jieba.cut(texts, cut_all=False)  # 返回的是一个迭代器
    for word in word_generator:
        #words_list += ' '.join(jieba.cut(texts, cut_all=False))
        words_list.append(word)
    return ' '.join(words_list)  # 注意是空格
    #return words_list


text = stop_words(text)

wc.generate(text)
# 基于彩色图像生成相应彩色
#image_colors = ImageColorGenerator(back_color)
# 显示图片
plt.imshow(wc)
# 关闭坐标轴
plt.axis('off')
# 绘制词云

#plt.axis('off')
plt.show()
# 保存图片
wc.to_file(r'E:\vscode_code\爬虫测试\json提取\京东\词云.png')