from aip import AipOcr
# 图片文字识别
APP_ID = '19082278'
APP_KEY = 'QWkx0oIWNoHuoer6f14PXDbq' # 公钥
SECRET_KEY = 'qXX5aTLKrDY9jyfCE171Q4zMTVl2ii8I' # 密钥
text_list = []

client = AipOcr(APP_ID, APP_KEY, SECRET_KEY)  # 初始化AipFace对象
with open(r'2.png','rb') as image:
	img_data = image.read()

text = client.basicGeneral(img_data)# 返回一个字典
# print(text)
for i in text.get('words_result'):
	text_list.append(i.get('words'))
	print(i.get('words'))
# print(text_list)
