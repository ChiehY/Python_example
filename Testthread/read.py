#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/6 11:51
# @Author  : YJ@SHOU
# @File    : read
# @Software: PyCharm


import threading
import os
import json
from bson.objectid import ObjectId
from pymongo import MongoClient


osm = MongoClient("mongodb://user:passwd@mongodb_url")#需要连接的mongodb数据库用户名及密码
db = osm.ship
col = db.shipData_up
s = col.find()
#print(s)
for item in s:
     #item = {col.find({"MMSI"})}
     #print(item)
     list=item["TRACK"]
     for i in range(0,len(list)):
          items = {
              "MMSI": item['MMSI'],
              "TRACK": []
          }
          lists={}
          if (float(list[i]['LAT']) > float(0) and float(list[i]['LAT']) < float(40)) and (
                       float(list[i]['LON']) > float(20) and float(list[i]['LON']) < float(75)):
              lists = {
                  "TIME": list[i]['TIME'],
                  "LAT": list[i]['LAT'],
                  "LON": list[i]['LON'],
                  "WAY": float(list[i]['WAY']),
                  "SPEED": float(list[i]['SPEED']),
                  "SID": list[i]['SID']
              }


     items["TRACK"].append(lists)
          #print (list[i])
     osm = MongoClient("mongodb://user:passwd@mongodb_url")
     db = osm.ship
     coll = db.shipData_in
     #print(item)
     item['_id'] = ObjectId()
     coll.insert(items)