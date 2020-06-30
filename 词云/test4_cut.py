# coding:utf8
import jieba
import wordcloud
# jieba分词处理句子

word_cloud = wordcloud.WordCloud(width=500,height=400,
	background_color='white',font_path='simsun.ttc')

txt = '华北科技学院位于河北省燕郊高新技术产业开发区，是中华人民共和国应急管理部直属高校，入选教育部“卓越工程师教育培养计划”、“新工科研究与实践项目” 、应急管理学院建设首批试点学校 、省级硕士学位授予单位立项建设单位、河北省院士工作站建站单位，为CDIO工程教育联盟成员单位、联合国教科文组织中国创业教育联盟理事单位'
txt_list = jieba.lcut(txt)
txt_str = ' '.join(txt_list)

word_cloud.generate(txt_str)

word_cloud.to_file('test4.png')