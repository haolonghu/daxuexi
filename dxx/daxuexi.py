import cv2
from PIL import ImageFont,ImageDraw,Image
import numpy as np
import requests

url=input("请输入对应的大学习连接：")
str1=input("请输入是第几期：")
url=url[:-10]
url=url+'images/end.jpg'

def produceImage(file_in, width, height, file_out):
    image = Image.open(file_in)
    resized_image = image.resize((width, height), Image.ANTIALIAS)
    resized_image.save(file_out)

#先爬取大学习截图
html=requests.get(url)
with open('sucai\\1.jpg', 'wb') as file:
    file.write(html.content)
    
#先对图片进行大小调整
file_in = 'sucai\\1.jpg'
width = 1080
height = 1841
file_out = 'sucai\\1.jpg'
produceImage(file_in, width, height, file_out)
             
#在图片指定位置加上字
bk_img = cv2.imread("sucai\\tou.jpg")
#设置需要显示的字体
fontpath = "sucai\\微软雅黑Light.ttc"
font = ImageFont.truetype(fontpath, 32)
img_pil = Image.fromarray(bk_img)
draw = ImageDraw.Draw(img_pil)
#绘制文字信息
ft = ImageFont.truetype("sucai\\微软雅黑Light.ttc", 45)
draw.text((768,155),str1, font = ft,fill = (0,0,0))
draw.text((769,156),str1, font = ft,fill = (0,0,0))
draw.text((770,157),str1, font = ft,fill = (0,0,0))
bk_img = np.array(img_pil)

#cv2.imshow("add_text",bk_img)
cv2.waitKey()
cv2.imwrite("sucai\\add_text.jpg",bk_img)

#开始拼接图片
img1 = cv2.imread('sucai\\add_text.jpg',1)
img2 = cv2.imread('sucai\\1.jpg',1)
img3 = cv2.imread('sucai\\wei.jpg',1)
result = np.vstack([img1,img2,img3])
cv2.imwrite("result.jpg",result)
print("\n生成成功，存为了result.jpg!")
