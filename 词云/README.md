学习内容来自哔哩哔哩：(同济子豪兄)[https://www.bilibili.com/video/BV1i4411W76Z?p=12]  

##### 常用参数

- width 词云图片宽度，默认400像素

- height 词云图片高度 默认200像素

- background_color 词云图片的背景颜色，默认为黑色

  `background_color='white'`

- font_step 字号增大的步进间隔 默认1号

  font_path 指定字体路径 默认None，对于中文可用`font_path='msyh.ttc'`、font_path='simsun.ttc'

- mini_font_size 最小字号 默认4号

- max_font_size 最大字号 根据高度自动调节

- max_words 最大词数 默认200

- stop_words 不显示的单词 `stop_words={"python","java"}`
- Scale 默认值1。值越大，图像密度越大越清晰(分辨率也增大)
- prefer_horizontal：默认值0.90，浮点数类型。表示在水平如果不合适，就旋转为垂直方向，水平放置的词数占0.9？
- relative_scaling：默认值0.5，浮点型。设定按词频倒序排列，上一个词相对下一位词的大小倍数。有如下取值：“0”表示大小标准只参考频率排名，“1”如果词频是2倍，大小也是2倍

- mask 指定词云形状图片，默认为矩形

- fit_words(字典) 根据词频生成词云
- generate(text)  根据文本生成词云
- generate_from_frequencies(字典) 根据词频生成词云
- generate_from_text(text)    根据文本生成词云