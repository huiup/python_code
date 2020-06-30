
import wordcloud
import jieba
import imageio
# 自定义词云背景图(China地图)

mk = imageio.imread(r"image\chinamap.png")
# mask:指定词云形状图片，默认为矩形
word_cloud = wordcloud.WordCloud(width=500,height=400,
	background_color='white',font_path='simsun.ttc',
	mask=mk)
# 引入文件的方式获取内容
with open(r'txt\关于实施乡村振兴战略的意见.txt',encoding='utf-8') as f:
	doc = f.read()

txt_list = jieba.lcut(doc)
txt_str = ' '.join(txt_list)

word_cloud.generate(txt_str)

word_cloud.to_file('test7.png')