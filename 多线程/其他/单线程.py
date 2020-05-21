import requests
import json,os
import lxml
from lxml import etree
 
#起始网页 https://tuchong.com/explore/
 
header = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',}
 
for i in range(1,20):
    url_temp='https://tuchong.com/rest/tags/%E8%87%AA%E7%84%B6/posts?page={}&count=20&order=weekly'.format(i)
    response = requests.get(url_temp,headers=header)
    html = json.loads(response.text)
    content_li = html['postList']
    for content in content_li:
        item={}
        item['title']=content['title']if len(content['title']) >0 else None
        item['view']=content['views']
        images_id=content['images']
        for img in images_id:
            #print(img)
            user_id = img['user_id']
            img_id = img['img_id']
            img_url = 'https://photo.tuchong.com/{}/f/{}.jpg'.format(user_id, img_id)
            print(img_url)
 
 
            if not os.path.exists('download'):
                os.mkdir('download')
 
            title = 'download/' +str(img_id)
            filename = img_url.split('/')[-1]
            response = requests.get(img_url)
               
            #保存图片名字有问题，不知道会不会重复
            with open(title+'.jpg', 'wb') as f:
                f.write(response.content)
