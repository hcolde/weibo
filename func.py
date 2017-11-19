# -*- coding: utf-8 -*-
'''
Author: hcolde

date: 2017.11.19

'''
import json
import re

#获取微博总数
def GetTotal(text):
	json_code = json.loads(text) #转化成json格式
	cardlistInfo = json_code['cardlistInfo']
	total = cardlistInfo['total']
	return total

#获取微博以&发布的时间
def GetAll(text):
	weibo_list = []
	time_list = []
	json_code = json.loads(text)
	cards = json_code['cards']

	#cards有值
	if cards:
		for count in cards:
			#如果存在mblog键
			if 'mblog' in count:
				content = Formate(count['mblog']['text']) #格式化
				time = count['mblog']['created_at']
				weibo_list.append(content)
				time_list.append(time)
			else:
				continue

		return weibo_list, time_list

	#cards为空
	else:
		return False, False

#去除html标签&缩进
def Formate(text):
	pattern = re.compile(r'</?[^>]*>')
	str1 = pattern.sub('', text)
	str2 = str1.replace(u'\u200b', '')
	return str2