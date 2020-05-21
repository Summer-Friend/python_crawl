'''
@Author: your name
@Date: 2020-03-07 11:53:35
@LastEditTime: 2020-03-07 12:09:27
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \vscode_code\练习\斗鱼\1.py
'''
import requests
import json
import csv
 
count = 1
base_url = "https://www.douyu.com/gapi/rkc/directory/0_0/"
 
#存放数据路径
#csv的a+性质表示追加，这个和pandas的to_csv的mode='a'是一样的道理
csv_file = open(r'E:\vscode_code\练习\斗鱼\douyu2_data.csv', 'w', newline='', encoding='utf-8-sig')  # 解决中文乱码问题
writer = csv.writer(csv_file)
writer.writerow(['名称', '类型', '主播', '热度'])
#请求200页数据
while count < 300:
    request_url = base_url + str(count)
    response = requests.get(request_url)
    # load json data
    json_data = json.loads(response.text)
    for host_info in json_data["data"]["rl"]:
        # 解析json里面的房间名，房间类型，主播名称，房间人数
        home_name = host_info["rn"].replace(" ", "").replace(",", "")
        home_type = host_info["c2name"]
        host_name = host_info["nn"]
        home_user_num = host_info["ol"]
        # print "\033[31m房间名：\033[0m%s，\033[31m房间类型：\033[0m%s，\033[31m主播名称：\033[0m%s，\033[31m房间人数：\033[0m%s"\
        #       % (home_name, home_type, host_name, home_user_num)
        #写入文件中
        writer.writerow([home_name, home_type, host_name, str(home_user_num)])
    print('正在写入第'+str(count)+'页')
    count += 1
