import hashlib
import base64
import requests
import  time
import json
import sys
from cookie_yzm import  getYzm
from oucSpider import  getCouse
from  oucSpider import  getApplication
# 账号和密码
userid = {
    'username': '这里填入学号',
    'password': '这里填入密码'
}

# 验证码
randnumber = ''
# 验证码地址 登录地址 课表地址
yzm_url = "http://jwgl.ouc.edu.cn/cas/getValidateCode"
login_url = 'http://jwgl.ouc.edu.cn/cas/login.jsp'


headers = {
    'Accept': 'text/plain, */*; q=0.01',
    'Accept-Encoding': 'gzip, deflate, sdch',
    'Accept-Language': 'zh-CN,zh;q=0.9,fr-FR;q=0.8,fr;q=0.7,zh-TW;q=0.6,en;q=0.5',
    'Connection': 'keep-alive',
    'Content-Length': '203',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Cookie': '333',
    'DNT': '1',
    'Host': 'jwgl.ouc.edu.cn',
    'Origin': 'http://jwgl.ouc.edu.cn',
    'Referer': 'http://jwgl.ouc.edu.cn/cas/login.action',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest'
}

def base64encode(message):
    encodestr = base64.b64encode(message.encode('GBK'))
    return encodestr

def doLogin():
    randnumber =  input("请输入验证码:")
    p_username = "_ubyrq" 
    p_password = "_pbyqy" 
    _sessionid = headers['Cookie']
    password = base64encode(base64encode(userid['password']) + hex_md5(randnumber+_sessionid))
    username = hashlib.md5(userid['username'] + _sessionid)
    datas = {
        p_username: username,
        p_password: password,
        'randnumber': randnumber,
        'isPasswordPolicy': '1',
        'txt_mm_expression': '13',
        'txt_mm_length': '7',
        'txt_mm_userzh': '0'
    }
    # print("使用Cookie", _sessionid)
    res = requests.post(url=login_url, headers=headers, data=datas)
    resmsg  = json.loads(res.text)
    if resmsg['status']!='200':
        print("登录遇到了问题: \n fuck you", res.text)
        sys.exit(0)
    print(res.text)

if __name__ == '__main__':
    # xn 就是年份    xq 夏季  0  秋季 1 春季 2   xh 就是学号
    params = "xn="+ "2019" + "&xq="+"1" + "&xh=" + userid['username']
    couse_url = "http://jwgl.ouc.edu.cn/student/wsxk.xskcb.jsp?params=" + base64encode(params).decode()
    application_url = "http://jwgl.ouc.edu.cn/taglib/DataTable.jsp?tableId=" + '6149'
    headers['Cookie'] = getYzm(yzm_url)
    doLogin()
    print('你要获取什么? 1. 课表  2. 选课结果')
    choice = input()
    time_start = time.time()
    if choice == '1':
        getCouse(couse_url, headers['Cookie'])
    else:
        getApplication(application_url, headers['Cookie'])
    time_end = time.time()
    print('totally cost', (time_end - time_start)*1000,"ms")
