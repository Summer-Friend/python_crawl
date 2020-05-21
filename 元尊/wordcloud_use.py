'''
@Author: your name
@Date: 2020-03-02 18:02:38
@LastEditTime: 2020-03-03 22:41:46
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \vscode_code\爬虫测试\元尊\wordcloud.py
'''
import pandas as pd 
import numpy as np 
from wordcloud import WordCloud
import matplotlib.pyplot as plt 
from PIL import Image

mask = np.array(Image.open('爬虫测试\元尊\元尊.jpg'))
text = "a b c s dasd as AAA A 啊牛逼 你比 牛逼 aaa ff s 数电 模电"
wordcloud = WordCloud(background_color="white",width=1000,height=860, mask = mask).generate(text)

#显示生成的词云 
plt.imshow(wordcloud)
plt.axis("off") 
plt.show() 

