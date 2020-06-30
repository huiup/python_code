from PIL import Image, ImageDraw, ImageFont
import cv2
import os

font_size = 7
text = "张"
# img_path = "D://bg.png"
#img_path = "D://のみこ - Bad Apple!! 00_00_00-00_03_41_00092.jpg"
directory_name = "F://steam/steamapps/workshop/content/431960/884307090/imgs/"


def character_generator(text):
    while True:
        for i in range(len(text)):
            yield text[i]


ch_gen = character_generator(text)
for filename in os.listdir(directory_name):
    print(filename+"添加成功！")  # 仅仅是为了测试
    img_path = directory_name + "/"+filename
    img_raw = Image.open(img_path)
    img_array = img_raw.load()
    img_new = Image.new("RGB", img_raw.size, (155, 155, 155))
    draw = ImageDraw.Draw(img_new)
    font = ImageFont.truetype('C:/Windows/fonts/Dengl.ttf', font_size)
    for y in range(0, img_raw.size[1], font_size):
        for x in range(0, img_raw.size[0], font_size):
            draw.text((x, y), next(ch_gen), font=font, fill=img_array[x, y], direction=None)

    img_new.convert('RGB').save("D://test2/"+filename)