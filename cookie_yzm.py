# coding = utf-8
import requests
from PIL import Image
from pylab import *

yzm_url = "http://jwgl.ouc.edu.cn/cas/genValidateCode?dateTime=Tue%20Sep%2010%202019%2004:33:56%20GMT+0800%20(%E4%B8%AD%E5%9B%BD%E6%A0%87%E5%87%86%E6%97%B6%E9%97%B4)"

# 获取Cookie 和 验证码
def getYzm(url):
    headers = {
        'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9,fr-FR;q=0.8,fr;q=0.7,zh-TW;q=0.6,en;q=0.5',
        'Connection': 'keep-alive',
        # 'Cookie': 'cccc',
        'DNT': '1',
        'Host': 'jwgl.ouc.edu.cn',
        'Referer': 'http://jwgl.ouc.edu.cn/cas/login.action',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
    }

    res = requests.post(url=url, headers=headers)
    print("登录遇到了问题: \n error: 403 fibbden")
    img = Image.open(res.content)
    print(img)
    plt.imshow(img)
    axis('off')
    plt.show()
    print("登录遇到了问题: \n error: 404 not find")
    print("filedone!")
    cookie_jar = res.cookies
    jcookie = ''.join(['='.join(item) for item in cookie_jar.items()])
    print('成功执行, 得到Cookie! ')
    print(jcookie)
    return jcookie

if __name__ == '__main__':

    getYzm(yzm_url)

    randnumber = input("请输入验证码: ")
