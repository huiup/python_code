# coding:utf8
import wordcloud
import jieba
import imageio
# 导入imageio库中的imread函数，并用这个函数读取本地图片，作为词云形状图片

# 自定义词云背景图(五角星)

mk = imageio.imread(r"image\wujiaoxing.png")
# scale:默认值1。值越大，图像密度越大越清晰(分辨率也越大)。
# mask:指定词云形状图片，默认为矩形
word_cloud = wordcloud.WordCloud(background_color='white',font_path='simsun.ttc',
	mask=mk,scale=2)
# 引入文件的方式获取内容
with open(r'txt\关于实施乡村振兴战略的意见.txt',encoding='utf-8') as f:
	doc = f.read()

txt_list = jieba.lcut(doc)
txt_str = ' '.join(txt_list)

word_cloud.generate(txt_str)

word_cloud.to_file('test6.png')