# -*- coding: utf-8 -*-
'''
Author: hcolde

date: 2017.11.19

'''

import xlwt
import time
import os

class Save():

	def __init__(self, path = '', name = str(time.strftime('%Y-%d-%m %H-%M-%S', time.localtime())), sheet_name = 'sheet 1'):
		self.path = path
		self.name = name +'.xls'
		self.workbook = xlwt.Workbook()
		self.sheet = self.workbook.add_sheet(sheet_name)

	def Write(self, text, row, col):
		self.sheet.write(row, col, text)

		#下一次从第几行开始写入
		return row + 1

	def Finish(self):
		self.workbook.save(self.path + os.sep + self.name)

'''
test code:

if __name__ == '__main__':
	s = Save(path = r'C:/Users/Administrator/Desktop', name = '666')
	s.Write('123', 0, 0)
	s.Finish()
'''