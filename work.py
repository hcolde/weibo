# -*- coding: utf-8 -*-
'''
Author: hcolde

date: 2017.11.19

'''
from spider import Spider
from save import Save
from func import GetTotal, GetAll
import time

if __name__ == '__main__':
	url = r'https://m.weibo.cn/api/container/getIndex?uid=2754693685&luicode=20000174&type=uid&value=2754693685&containerid=1076032754693685&page='
	page = 1
	headers = {'User-Agent': r'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.5) Gecko/20091102 Firefox/3.5.5 (.NET CLR 3.5.30729)'}
	spider = Spider(headers = headers)

	while not spider.Get(url + str(page)):
		time.sleep(3)

	total = GetTotal(spider.Text())
	save = Save(name = 'weibo')
	row = 0

	#微博总数随时变化，故多爬50页
	for count in range(1, total + 51):
		page = str(count)
		while not spider.Get(url + page):
			time.sleep(3)

		weibo, time = GetAll(spider.Text())

		#如果该页面有内容
		if weibo:
			for i in range(0, len(weibo)):
				save.Write(time[i], row, 0)
				row = save.Write(weibo[i], row, 1)

		#如果该页面没有内容，则不需要继续爬取接下来的页面
		else:
			break
	save.Finish()
	print('Report:The work is done.')


