# coding:utf8
import imageio
import wordcloud
# 设置词云图片的轮廓

mk = imageio.imread(r"image\alice.png")

# 增加参数contour_width和contour_color设置轮廓宽度和颜色
word_cloud = wordcloud.WordCloud(background_color="white",
                        mask=mk,
                        contour_width=1,
                        contour_color='steelblue')
# 文件内容为英文
with open(r'txt\hamlet.txt') as f:
	doc = f.read()
word_cloud.generate(doc)

word_cloud.to_file('test9.png')