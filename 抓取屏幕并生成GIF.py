from time import sleep
from PIL import ImageGrab,Image

m = int(input("输入抓取时间（min）："))
m = m * 60
n = 1
#循环生成图片
while n < m:
    sleep(0.02)
    im = ImageGrab.grab()
    local = (r"%s.jpg" % (n))
    im.save(local,'jpeg')
    n = n + 1
#读取生成的图片并排序
listjpg = [x for x in os.listdir() if re.search(r'jpg$',x)]
'''列表字符串元素固定位置为数字，以"."为分隔符，在数字后面
可以使用两个字符为分隔符，分别为数字前后的字符，例：a，b分别为数字前后的字符 listjpg.sort(key= lambda x:int(x.split('b')[0].split('a')[1]))'''
listjpg.sort(key= lambda x:int(x.split('.')[0]))
#生成gif
im = Image.open('1.jpg')
images = []
for i in listjpg:
    images.append(Image.open(i))
im.save('gif.gif',save_all=True,append_images=images,loop=1,duration=1,comment=b"aaabb")
