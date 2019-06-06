import csv
import json
import time
from urllib.request import urlopen

csvfile = open('test111.csv', 'r', encoding='UTF-8')
csvreader = csv.reader(csvfile)
final_list = list(csvreader)
final_list.__delitem__(0)

adds = final_list
orgin_name = adds[0][0]
orgin_lat_lng = str(round(float(adds[0][2]), 5)) + ',' + str(round(float(adds[0][1]), 5))

ak = 'Gh0oXBEsI0tH7X0dUMSdcDKu'
url_source = 'http://api.map.baidu.com/direction/v2/driving?origin='

res_list = []
name_attribute = ['源地址', '目的地址', '驾车距离', '驾车时间']
res_list.append((name_attribute))

for i in range(1, len(adds)):
    destination_name = adds[i][0]
    destination_lat_lng = str(round(float(adds[i][2]), 5)) + ',' + str(round(float(adds[i][1]), 5))
    url_full = url_source + orgin_lat_lng + '&destination=' + destination_lat_lng + '&ak=' + ak
    request = urlopen(url_full)
    result = request.read().decode()
    temp = json.loads(result)
    time.sleep(1)

    if temp['status'] == 0:
        distance = temp['result']['routes'][0]['distance']  # 获取驾车距离
        duration = temp['result']['routes'][0]['duration']  # 获取驾车时间
        res_list.append([orgin_name, destination_name, distance, duration])
    else:
        print("没找到驾车路线")
        res_list.append([orgin_name, destination_name, '0', '0'])

try:
    if temp['status'] == 0:
        csvfile_distance = open('result_distance.csv', 'w+', encoding='UTF-8', newline='')
        writer = csv.writer(csvfile_distance)
        for i in range(len(res_list)):
            writer.writerow(res_list[i])
finally:
    csvfile_distance.close()