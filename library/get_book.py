import json
import requests
import sys

postUrl = 'http://222.195.226.30/opac/ajax_search_adv.php'
# payloadData数据
payloadData = {
    'afnPriceStr': 10,
    'currency':'USD',
    'productInfoMapping': {
        'asin': 'B072JW3Z6L',
        'dimensionUnit': 'inches',
    }
}
# 请求头设置
payloadHeader = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Content-Type': 'application/json',
    'DNT': '1',
    'Origin': 'http://222.195.226.30',
    'Referer': 'http://222.195.226.30/opac/search_adv.php',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest'
}
headers = {
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
'Accept-Encoding': 'gzip, deflate',
'Accept-Language': 'zh-CN,zh;q=0.9,fr-FR;q=0.8,fr;q=0.7,zh-TW;q=0.6,en;q=0.5',
'Connection': 'keep-alive',
'Cookie': 'PHPSESSID=n5b3d9op3hcgjfbieqn7sjp6d7',
'DNT': '1',
'Host': '222.195.226.30',
'Upgrade-Insecure-Requests': '1',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'
}

searchbook = '垃圾'
index = 1

def get_book_search(index):
        dumpJsonData = '{"searchWords":[{"fieldList":[{"fieldCode":"02","fieldValue":"' + searchbook + '"}]}],"filters":[],"limiter":[],"sortField":"relevance","sortType":"desc","pageSize":20,"pageCount":' + str(index) + ',"first":true}'

        res = requests.post(postUrl, data=dumpJsonData.encode('utf-8'), headers=payloadHeader)
        content = json.loads(res.text)['content']
        if index == 1:
            print('共有:', json.loads(res.text)['total'], '条结果. \n')
        for item in range(len(content)):
            print(json.dumps(content[item], ensure_ascii=False, indent=2))

            urlstatus = 'http://222.195.226.30/opac/ajax_isbn_marc_no.php?marc_no='\
                 +content[item]['marcRecNo']+'&rdm=13515&isbn='+ \
                 content[item]['isbn']
            getr = requests.get(url=urlstatus,headers=headers)

            print(json.loads(getr.text)['lendAvl'])

            key = input('下一个? 1. 是  2. 否 default: exit\n')
            if key == '1' :
                continue
            elif key == '2':
                break
            else:
                sys.exit(0)
        print(index)

if __name__ == '__main__':
    searchbook = input('输入要查找的书:')
    while 1:
        get_book_search(index)
        chose = input('是否下一页? 1. 是 2. 否 default: 退出程序\n')
        if chose == '1':
            index += 1
        elif chose == '2' :
            break
        else:
            sys.exit(0)
