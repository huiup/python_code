# coding:utf8
import wordcloud
import jieba
# 文件+分词


# 自定义设置词云图片的宽、高、背景颜色、字体
word_cloud = wordcloud.WordCloud(width=500,height=400,
	background_color='white',font_path='simsun.ttc')
# 引入文件的方式获取内容
with open(r'txt\关于实施乡村振兴战略的意见.txt',encoding='utf-8') as f:
	doc = f.read()

txt_list = jieba.lcut(doc)
txt_str = ' '.join(txt_list)

word_cloud.generate(txt_str)

word_cloud.to_file('test5.png')