# coding = utf-8
import requests
from bs4 import BeautifulSoup as bs

dates = ["11", "12", "13", "14", "15",
         "21", "22", "23", "24", "25",
         "31", "32", "33", "34", "35",
         "41", "42", "43", "44", "45",
         "51", "52", "53", "54", "55",
         "61", "62", "63", "64", "65",
         "71", "72", "73", "74", "75"]

week = ["一", "二", "三", "四", "五", "六", "七"]

onCouse = ["  一二", "  三四", "  五六", "  七八", "  九十"]

# 访问教务处得到课表
def getCouse(url, cookie):
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9,fr-FR;q=0.8,fr;q=0.7,zh-TW;q=0.6,en;q=0.5',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Cookie': cookie,
        'DNT': '1',
        'Host': 'jwgl.ouc.edu.cn',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
    }
    r = requests.get(url=url, headers=headers)
    if r.status_code!=200:
        print(r.status_code, '未成功登录!')
        return
    html = r.text
    # 解析html代码
    soup = bs(html, 'lxml')
    for date in dates:
        couse = soup.find(attrs={'id': 'k11'}).find(name="div")
        if couse == None:
            continue
        couseStr =str(couse)
        start = couseStr.find("<br/>", 0, len(couseStr))
        end = couseStr.find("</div>", start, len(couseStr))
        wid = int(date[0])-1
        cid =  int(date[1]) -1
        print("课程周"+ week[wid] + onCouse[cid]  + "节:  " + couse.find(name='b').string)
        print("授课老师: "+ couseStr[start+5: end])

    print('成功执行!')

# 获取选课申请结果
def getApplication(url, cookie):
    headers = {
                'Accept': 'text / html, application / xhtml + xml, application / xml;q = 0.9, image / webp, image / apng, * / *;q = 0.8, application / signed - exchange;v = b3',
                'Accept - Encoding': 'gzip, deflate',
                'Accept - Language': 'zh - CN, zh;q = 0.9, fr - FR;q = 0.8, fr;q = 0.7, zh - TW;q = 0.6, en;q = 0.5',
                'Cache - Control': 'max - age = 0',
                'Connection': 'keep - alive',
                'Content - Length': '90',
                'Content - Type': 'application / x - www - form - urlencoded',
                'Cookie': cookie,
                'DNT': '1',
                'Host': 'jwgl.ouc.edu.cn',
                'Origin': 'http: // jwgl.ouc.edu.cn',
                'Referer': 'http: // jwgl.ouc.edu.cn / student / wsxk.yxkcsq.html?menucode = JW130411',
                'Upgrade - Insecure - Requests': '1',
                'User - Agent': 'Mozilla / 5.0(WindowsNT10.0;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 76.0.3809.132Safari / 537.36'
    }
    datas = {
        'xktype': '9',
        'xh': '18030022015',
        'xn': '2019',
        'xq': '1',
        'nj': '2017',
        'zydm': '0032',
        'items': '',
        'kcfw': 'All'
    }
    r = requests.post(url=url, headers=headers, data=datas)
    print(r)
    if r.status_code != 200:
        print(r.status_code, '未成功登录!')
        return
    html = r.text
    # 解析html代码
    soup = bs(html, 'lxml')
    soup = soup.find(name="tbody")
    number = 0
    while number < 20:
        application = soup.find(attrs={'id': 'tr' + number})
        if application == None:
            continue
        couse_name = application.find(attrs={'name': 'kc' }).find(name="a").string
        status = application.find(attrs={'name' : 'apply_status'}).string
        teacher_name = application.find(attrs={'name' : 'rkjs'}).find(name="a").string
        number +=1
        print('课程:',couse_name, '任课教师:', teacher_name, '状态:', status)

    print('成功执行!')

