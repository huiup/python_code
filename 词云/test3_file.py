# coding:utf8
import wordcloud
# 导入文件内容

word_cloud = wordcloud.WordCloud(width=500,height=400,
	background_color='white',font_path='simsun.ttc')
# 引入文件的方式获取内容
with open(r'txt\关于实施乡村振兴战略的意见.txt',encoding='utf-8') as f:
	doc = f.read()

word_cloud.generate(doc)

word_cloud.to_file('text3.png')