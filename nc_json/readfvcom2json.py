from netCDF4 import Dataset
import json
import datetime
import numpy as np

def dataFormat(xLAT, xLONG, Htime, fileList, variablesList):
    result = []
    for file in fileList:
        filePath = file
        nc = Dataset(filePath, mode='r')

        xlats = nc.variables['latc'][:]
        xlongs = nc.variables['lonc'][:]

        #calculate  distance
        indexLAT = np.array(xlats-xLAT) * np.array(xlats-xLAT)
        indexLONG = np.array(xlongs - xLONG) * np.array(xlongs - xLONG)
        distance=np.array(indexLONG)+np.array(indexLAT)

        #find min_distance_index
        def find_all_index(arr, item):
            return [i for i, a in enumerate(arr) if a == item]

        indexmin=find_all_index(distance,distance.min())
        # print(indexmin)

        for variable in variablesList:
            data = nc.variables[variable][:]
            result.append(float(data[Htime][0][indexmin]))

    return result

dataResult = dataFormat(21, 114, 0,['file_url_path'], ['u','v']) #file_url_path需要转换的文件所在地

with open('test.json', 'w') as f:
    json.dump(dataResult, f)

