#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  spider.py
#  
#  Copyright 2019 billy huang <billy huang@DESKTOP-77CQ0AV>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  



import requests 
import json
with open('headers.json') as f:
   headers = f.read()
   headers = eval(headers)
#headersֱ��F12��ת��networks��Ȼ��ѡ��һ��steamcommunity.com
url= 'https://steamcommunity.com/market/pricehistory/?appid=753&market_hash_name=753-Sack of Gems' 
strhtml=requests.get(url,headers=headers,verify=False) 
content = json.loads(strhtml.text)
filename = 'Gems.json'
with open(filename,'w',encoding='utf-8') as name:
   name.write(str(content))
print('spider got them!")
