import requests 
import ssl
from bs4 import BeautifulSoup
import os
import json

url = "https://ce.pknu.ac.kr/ce/1814"
req = requests.get(url, verify=False)
html = req.text

soup = BeautifulSoup(html, 'html.parser')

my_titles = soup.select(
    '#sbCont > div > table > tbody > tr > td.bdlTitle > a'
)




#새로운 정보 딕셔너리로 정제
new_data = {}
for title in my_titles :
    new_data[title.text] = title.get('href')


#저장되어 있던 이전 정보
# 만약 새로운 정보가 추가되어다면
    
updated_data = {}
with open('/Users/yoon/vscode/PKNUCrolling/result.json', 'r') as file:
    prev_datas = json.load(file)
    keys = new_data.keys() - prev_datas.keys()
    if len(keys) == 0: 
        for i in range(3):
            print()
        print("업데이트 사항 없음")
        for i in range(3):
            print()
    else :
        for i in range(3):
            print()
        for key in keys:
            print(url + new_data[key])
        for i in range(3):
            print()


            


    # 1. 새로운 정보 (타이틀, href) 리턴
    # 2. json file 에 해당 정보 추가.

# 만약 없다면 그냥 끝내기 


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# json 파일에 새로운 정보 저장하기 .
with open(os.path.join(BASE_DIR, 'result.json'), 'w+') as json_file:
    json.dump(new_data, json_file)


