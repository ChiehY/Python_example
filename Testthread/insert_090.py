import threading
import os
import json
from pymongo import MongoClient


def insertMG(files):
    osm = MongoClient("url", port)#mongodb地址及端口号
    db = osm.ship
    col = db.shipData_test

    for file in files:
        with open(file, 'r') as f:
            try:
                dic = {
                    "MMSI": file.split("/")[-1].split(".")[0],
                    "TRACK": []
                }

                for line in f.readlines():
                    q = line.split(";")
                    tempJ = {
                        "TIME": q[1],
                        "LAT": q[2],
                        "LON": q[3],
                        "WAY": float(q[4]),
                        "SPEED": float(q[5]),
                        "SID": q[6]
                    }
                    dic["TRACK"].append(tempJ)

                col.insert_one(dic)
            except:
                print("%s ERROR at %s" %(file, line))

       # print("%s inserted." %(file))


path = './'
Index = []

if not os.path.isdir('./index'):
    os.mkdir('./index')

for root, dirs, files in os.walk(path):
    if root.startswith('./allshipsin2017_trajectory'):
        for file in files:
            if file.endswith('txt'):
                Index.append(os.path.join(root, file))
    else:
        continue

while '' in Index:
    Index.remove('')

splitIndex = [Index[i: i + 6000] for i in range(0, len(Index), 6000)]


class myThread(threading.Thread):
    def __init__(self, threadID, name, counter, files):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
        self.files = files
    def run(self):
        print ("Start Thread：" + self.name)
        insertMG(self.files)
        print ("Stop Thread：" + self.name)

createVar = locals()

# Create Threads
for i in range(0, len(splitIndex)):
    files = splitIndex[i]
    createVar["thread%d" %(i)] = myThread(i, "Thread-%s" %(i), i, files)

# Start Threads
for i in range(0, len(splitIndex)):
    createVar["thread%d" % (i)].start()

for i in range(0, len(splitIndex)):
    createVar["thread%d" % (i)].join()

print ("Back to Main Thread.")
