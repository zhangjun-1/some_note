#简单爬虫，下载豆瓣图片
import urllib.request
import re

def get_html_code(url):     #传入url，获取url的html源代码
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebkit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36 Edg/87.0.664.47'
    }       #模拟64位Windows的edge浏览器访问
    request = urllib.request.Request(url, headers=headers)      #Request函数将url添加到头部
    page = urllib.request.urlopen(request).read()       #将url页面的源代码保存成字符串
    page = page.decode('UTF-8')         #字符串转码
    return page

def get_img(page):          #由html源代码获取图片url，将图片下载到本地
    imgList = re.findall(r'http.+\.jpg',page)       #re.findall(pattern,string,flags=0)搜素字符串，以列表返回全部匹配的子串
    print(imgList)
    x = 0
    for imgUrl in imgList:      #遍历url列表
        try:
            print('正在下载： {}'.format(imgUrl))
            urllib.request.urlretrieve(imgUrl, 'D:/img/%d.png' %x)      #urlretrieve(url,local)方法根据图片url把图片下载到本地
            x += 1
        except:
            continue


if __name__ == '__main__':
    url = 'http://movie.douban.com/top250'          #豆瓣电影 Top250的url
    page = get_html_code(url)
    get_img(page)
