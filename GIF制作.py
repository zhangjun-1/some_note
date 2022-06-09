from PIL import Image
im = Image.open('img/1.png')
images = []
images.append(Image.open('img/2.png'))
images.append(Image.open('img/test.jpg'))
im.save('gif.gif',save_all=True,append_images=images,loop=1,duration=1,comment=b"aaabb")

