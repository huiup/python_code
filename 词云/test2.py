# coding:utf8
import wordcloud
# 自定义设置词云图片的宽、高、背景颜色、字体

word_cloud = wordcloud.WordCloud(width=500,height=400,
	background_color='white',font_path='simsun.ttc')

word_cloud.generate(r'我是孙行者的兄弟，闻说你拿了我家兄，却来与你寻事的。”二魔道：“是我拿了，锁在洞中。你今既来，必要索战。我也不与你交兵，我且叫你一声，你敢应我么？”行者道：“可怕你叫上千声，我就答应你万声！”')

word_cloud.to_file('text2.png')