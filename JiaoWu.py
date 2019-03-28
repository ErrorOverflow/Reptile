# -*- coding: utf-8 -*-
import requests
import re
from bs4 import BeautifulSoup
import xlwt

header = {
    'Host': '10.200.21.61:7001',
    'Connection': 'keep-alive',
    'Content-Length': '112',
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'
                  ' Chrome/73.0.3683.86 Safari/537.36',
    'Origin': 'http://10.200.21.61:7001',
    'Content-Type': 'application/x-www-form-urlencoded',
    'DNT': '1',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,'
              'application/signed-exchange;v=b3',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh,zh-TW;q=0.9,en-US;q=0.8,en;q=0.7,zh-CN;q=0.6',
    'Cookie': 'JSESSIONID=EE08EF23B5F17A9D9B3FBB20CDED5FE7'}
url = "http://10.200.21.61:7001/ieas2.1/xsxk/queryXsxkList"

r = requests.get(url, headers=header, cookies={'JSESSIONID': 'EE08EF23B5F17A9D9B3FBB20CDED5FE7'})
print(r.status_code)
r.encoding = 'utf8'

data_list = []
print(r.text)
