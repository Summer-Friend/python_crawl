'''
@Author: your name
@Date: 2020-01-20 13:13:28
@LastEditTime : 2020-01-20 15:31:52
@LastEditors  : Please set LastEditors
@Description: In User Settings Edit
@FilePath: \vscode_code\爬虫测试\可视化\天气网.py
'''
import matplotlib as mpl
mpl.use('agg')
#matplotlib inline
import requests
import re
import pandas as pd
import time
import seaborn as sns
sns.set()
mpl.rcParams['font.sans-serif']=[u'SimHei']
mpl.rcParams['axes.unicode_minus']=False
def get_one_page(url, headers):
    '''
    抓取单个网页的源码
    '''
    # 添加headers参数是为了伪装成浏览器，避免被反爬虫策略封禁
    response = requests.get(url, headers=headers)
    # 200意味着成功的请求
    if response.status_code == 200:
        return response.content.decode('utf-8')
    return None
# 设置猫眼电影TOP100的url
# 为了方便，我们使用列表推导式来实现url的列举
urls = ['http://maoyan.com/board/4?offset={0}'.format(i) for i in range(0, 100, 10)]

# 用header来假装自己是浏览器，这一部分可以通过浏览器的检查功能来找到，不清楚的可以百度搜索一下，非常简单。
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3314.0 Safari/537.36 SE 2.X MetaSr 1.0'
}
# 先把所有网页源码爬下来
data = []
for url in urls:
    tmp = get_one_page(url, headers=headers)
    if not tmp == None:
        data.append(tmp)
    time.sleep(0.5)
# 我们查看一下爬取的网页数量是否符合预期
print('{0} pages crawled'.format(len(data)))
# 使用re.compile将各个正则表达式封装成正则表达式对象，方便后边解析使用。re.S参数是为了让'.'能匹配空格。
actor_pattern = re.compile('<p\sclass="star">\s*(.*?)\s*</p>', re.S)
title_pattern = re.compile('class="name".*?movieId.*?>(.*?)</a></p>', re.S)
index_pattern = re.compile('<dd>.*?board-index.*?>(\d+)</i>', re.S)
time_pattern = re.compile('<p\sclass="releasetime">(.*?)</p>', re.S)
score_pattern = re.compile('<p\sclass="score"><i\sclass="integer">(\d+)\.</i><i\sclass="fraction">(\d+)</i></p>', re.S)

# 使用列表来存储数据
indexes = []
actors = []
titles = []
release_times = []
scores = []

# 循环解析十个网页，将解析出来的数据附加在对应的列表中
for page in data:
    indexes.extend(re.findall(index_pattern, page))
    titles.extend(re.findall(title_pattern, page))
    actors.extend(re.findall(actor_pattern, page))
    release_times.extend(re.findall(time_pattern, page))
    scores.extend(re.findall(score_pattern, page))
# 清洗主演、上映时间、上映国家或地区、评分数据
actors = [i.strip('主演：') for i in actors]

# 可以看到，上映地区的数据在上映时间后边的括号里，有很多电影上映时间后边没有括号了，通过观察我们发现这些都是中国大陆上映的电影，
# 那我们就将这些默认缺失的部分补充为'中国'
locs = [i.strip('上映时间：')[10:].strip('()') if len(i.strip('上映时间：')) > 10 else '中国' for i in release_times]

# 我们把字符串中‘上映时间：’这些没用的去掉，然后取十位，也就是'YYYY-mm-dd'的长度，事实上这一步我们也可以在正则表达式中解决，
# 比如用'\d'匹配数字等，详细的大家可以自己尝试，这样还可以解决数据格式不符合预期的问题。
# 事实上电影天空之城的上映时间的格式还真的跟其他的不一样，不过此次我们不考虑这个问题
release_times = [i.strip('上映时间：')[:10] for i in release_times]

# 网页里边将分数的个位数与小数用了不同的格式，所以解析的时候我们分开提取了它们，因此需要处理一下
scores = [int(i) + int(j)/10 for i, j in scores]
# 生成DataFrame
df = pd.DataFrame({
    'rank': indexes,
    'title': titles,
    'actor': actors,
    'release_time': release_times,
    'score': scores,
    'location': locs
})
# 修改列名
df = df[['rank', 'title', 'actor', 'score', 'location', 'release_time']]
# 保存到本地csv文件中
df.to_csv('爬虫测试\maoyan\maoyan.csv', index=False)

# 展示一下数据
df.head()

# 我们的上映日期是以字符串存储的，需要将上映年份解析出来
df['上映年份'] = df['release_time'].map(lambda x: int(x[:4]))
df['上映年份'].value_counts()
print(df['上映年份'].value_counts())
#我们可以考虑以5年为一个区间将数据分布集中起来。
df['上映年份区间'] = pd.cut(df['上映年份'], bins=[1938, 1980, 1990, 1995, 2000, 2005, 2010, 2015, 2018])
df['上映年份区间'].value_counts().sort_index().plot(kind='bar')
