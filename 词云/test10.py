# coding:utf8
import matplotlib.pyplot as plt
from wordcloud import WordCloud,ImageColorGenerator
import imageio
# 按图片原颜色绘制词云


mk = imageio.imread(r"image\alice_color.png")

with open(r'txt\alice.txt') as f:
	doc = f.read()

word_cloud = WordCloud(background_color="white",
               mask=mk,)

word_cloud.generate(doc)

# 调用wordcloud库中的ImageColorGenerator()函数，提取模板图片各部分的颜色
image_colors = ImageColorGenerator(mk)

# 显示原生词云图、按模板图片颜色的词云图和模板图片，按左、中、右显示
fig, axes = plt.subplots(1, 3)# 1行、3列
# 最左边的图片显示原生词云图
axes[0].imshow(word_cloud)
# 中间的图片显示按模板图片颜色生成的词云图，采用双线性插值的方法显示颜色
axes[1].imshow(word_cloud.recolor(color_func=image_colors), interpolation="bilinear")
# 右边的图片显示模板图片
axes[2].imshow(word_cloud, cmap=plt.cm.gray)
for ax in axes:
    ax.set_axis_off()
plt.show()

# 给词云对象按模板图片的颜色重新上色
wc_color = word_cloud.recolor(color_func=image_colors)
# 将词云图片导出到当前文件夹
wc_color.to_file('test10.png')
