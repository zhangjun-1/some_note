from time import sleep
from PIL import ImageGrab,Image

m = int(input("输入抓取时间（min）："))
m = m * 60
n = 1
while n < m:
    sleep(0.02)
    im = ImageGrab.grab()
    local = (r"%s.jpg" % (n))
    im.save(local,'jpeg')
    n = n + 1
listjpg = [x for x in os.listdir() if re.search(r'jpg$',x)]
listjpg.sort(key= lambda x:int(x.split('.')[0]))

im = Image.open('1.jpg')
images = []
for i in listjpg:
    images.append(Image.open(i))
im.save('gif.gif',save_all=True,append_images=images,loop=1,duration=1,comment=b"aaabb")
