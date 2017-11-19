# -*- coding: utf-8 -*-
'''
Author: hcolde

date: 2017.11.18

'''

import requests
import random
import time

class Spider():

    def __init__(self, timeout = 6, proxies = None, headers = None, data = None, encoding = 'utf-8'):
        '''
        data: 数据
        timeout: 超时
        proxies: 代理
        headers: 请求头
        encoding: 编码

        '''
        self.data = data
        self.timeout = timeout
        self.proxies = proxies
        self.headers = headers
        self.encoding = encoding
        self.response = None

    def Get(self, url):
        if url:
            try:
                self.response = requests.get(
                    url,
                    data = self.data,
                    timeout = self.timeout,
                    proxies = self.proxies,
                    headers = self.headers
                )

                if self.response.status_code == 200:
                    self.response.encoding = self.encoding
                    return True

                else:
                    return False

            except requests.ConnectTimeout:
                print('尝试连接到远程服务器时请求超时')
                return False

            except requests.ReadTimeout:
                print('服务器没有在指定的时间内发送任何数据')
                return False

        else:
            print('请传入一个url')
            return False

    def Text(self):
        return self.response.text

'''
test code:

if __name__ == '__main__':
    headers = {'User-Agent': r'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.5) Gecko/20091102 Firefox/3.5.5 (.NET CLR 3.5.30729)'}
    url = 'http://ip.ws.126.net/ipquery'
    spider = Spider(headers = headers, encoding = 'gbk')
    if spider.Get(url):
        print(spider.Text())
'''