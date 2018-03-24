#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/8 12:59
# @Author  : YJ@SHOU
# @File    : read2
# @Software: PyCharm


from bson.objectid import ObjectId
from pymongo import MongoClient


osm = MongoClient("mongodb://user:passwd@mongodb_url")
db = osm.ship
col = db.shipData_up
s = col.find(no_cursor_timeout=True).batch_size(5)

for item in s:
     list = item["TRACK"]
     for i in range(0,len(list)):

          if (float(list[i]['LAT']) > float(-50) and float(list[i]['LAT']) < float(0)) and (
                       float(list[i]['LON']) > float(-20) and float(list[i]['LON']) < float(60)):
              MMSI = item['MMSI']
              items = {
                      "MMSI": MMSI,
                      "TRACK": []
                  }

              lists = {
                  "TIME": list[i]['TIME'],
                  "LAT": list[i]['LAT'],
                  "LON": list[i]['LON'],
                  "WAY": float(list[i]['WAY']),
                  "SPEED": float(list[i]['SPEED']),
                  "SID": list[i]['SID']
              }
              items["TRACK"].append(lists)

              osm = MongoClient("mongodb://user:passwd@mongodb_url")
              db = osm.ship
              coll = db.shipData_09
              #print(item)
              item['_id'] = ObjectId()
              coll.insert(items)
s.close()