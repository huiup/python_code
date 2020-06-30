
import wordcloud
import jieba
import imageio
# 设置文件中不需要建立词云的词(如：stopwords={'曹操','孔明'})

mk = imageio.imread(r"image\chinamap.png")
# mask:指定词云形状图片，默认为矩形
word_cloud = wordcloud.WordCloud(width=500,height=400,
	background_color='white',font_path='simsun.ttc',
	mask=mk,stopwords={'曹操','孔明'})
# 对来自外部文件的文本进行中文分词，得到string
with open(r'txt\三国演义.txt',encoding='utf-8') as f:
	doc = f.read()
txt_list = jieba.lcut(doc)
txt_str = ' '.join(txt_list)

word_cloud.generate(txt_str)

word_cloud.to_file('test8.png')