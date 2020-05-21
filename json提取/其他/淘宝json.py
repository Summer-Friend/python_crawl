'''
@Author: your name
@Date: 2020-02-27 16:39:54
@LastEditTime: 2020-02-27 17:04:57
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \vscode_code\爬虫测试\淘宝\淘宝json.py
'''
import requests
import json

url = 'http://rate.tmall.com/list_detail_rate.htm?itemId=41464129793&sellerId=1652490016&currentPage=1'

#url = 'https://rate.tmall.com/list_detail_rate.htm?itemId=577742170819&spuId=1064347164&sellerId=1130199603&order=3&currentPage=2&append=0&content=1&tagId=&posi=&picture=&groupId=&ua=098%23E1hvrpv4vfOvUvCkvvvvvjiPn2qwtjrERLzp0jYHPmPytjYWPFdUzj1PPLdwzjrWdphvmpvWkIaPLg1K5T6CvCh9CHvU%2BbmWb39idAIucweHQ46CvCh9CHW2L6GZnM%2BidAI3pQeHA46CvvyvCCg2qKgWF%2Bytvpvhvvvvv8wCvvpvvUmmRphvCvvvvvvPvpvhvv2MMQhCvvOvCvvvphvEvpCWvCiDvvakfwLvaB4AVAnlYExrj8td2ezpafm655DCgRoQ0fJ6EvLvqU0HKfE9ZKFEDaVTRogRD7zhs8TJEcqhsj7%2BhLIA7gkQiNoXV8yCvv9vvUvg17nRUgyCvvOUvvVvayRtvpvIvvvviZCvvvvvvvhvphvU3vvv99Cvpv32vvmmvhCvm8UvvUhdphvh%2BOwCvvpvCvvvdphvmpvhRObSqQpQx46CvvyvCCymEkOWcxTrvpvEvvonvkpy2m8Z9phv2Hi4dMJ6zHi4cJxyzT6CvvyvCj%2BmjB6WR5oCvpvZ7DSTYqcw7DiaGqP5MvC4aDdZzlvtvpvhvvvvv86CvvyvC2Wm7H9WwiJCvpvW7DKXm22w7DiaMFSNRphvCvvvvvmrvpvEvvp99zX0Fvg39phvHHiajhkqzHi4NNyQtsAU73H4raGB&needFold=0&_ksTS=1582792586017_695&callback=jsonp696'
headers = {
        'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.167 Safari/537.36'

    }

#headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)'
#           'Chrome/65.0.3314.0 Safari/537.36 SE 2.X MetaSr 1.0' }

# 使用request模块打开并获取网页内容
response = requests.get(url, headers=headers)   # 禁止重定向
#content = response.content

content = response.text
result = json.loads(content)
print(result)

'''
result = result['rateDetail']['rateCount']

csv_file = open(r'E:\vscode_code\爬虫测试\淘宝\taobao_data.csv', 'w', newline='', encoding='utf-8-sig')  # 解决中文乱码问题
writer = csv.writer(csv_file)
writer.writerow(['评价'])
for data in result:
    writer.writerow(data)
csv_file.close()
'''