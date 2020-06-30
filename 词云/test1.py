# coding:utf8
import wordcloud
# 默认运用

# 创建词云对象wword_cloud
word_cloud = wordcloud.WordCloud()

# 调用词云对象的generate方法，将文本传入
# 它会自动过滤掉废话(如：and that of the之类的没意义的词)
word_cloud.generate('and that government of the people, by the people, for the people, shall not perish from the earth.')

# 将生成的词云保存为output1.png图片文件，保存出到当前文件夹中
word_cloud.to_file('text1.png')