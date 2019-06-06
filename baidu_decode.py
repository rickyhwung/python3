import csv, json, os
from urllib.request import urlopen, quote

#通过百度地图接口，输入地址列表，返回经纬度里列表
def address_lat_lng(addresses, city="合肥市"):
    ak = 'Gh0oXBEsI0tH7X0dUMSdcDKu'
    url = 'http://api.map.baidu.com/geocoder/v2/?address='
    output = 'json'
    res_list = []
    # name_attribute = ['地址名称', '经度', '维度']
    # res_list.append(name_attribute)
    for add in addresses:
        city = quote(city)
        add0 = quote(add)
        url_full = url + add0 + '&output=' + output + '&ak=' + ak + '&city=' + city
        request = urlopen(url_full)
        result = request.read().decode()
        temp = json.loads(result)
        res_status = temp['status']
        confidence = temp['result']['confidence']

        if temp['status'] == 0:
            lng = temp['result']['location']['lng']  # 获取经度
            lat = temp['result']['location']['lat']  # 获取纬度
            res_list.append([add, lng, lat, confidence, res_status])
        else:
            print(add + "没找到")
            res_list.append([add, '', '', '', res_status])

    return res_list

def list_to_csv(lists, file_name):
    csvfile = open(file_name, 'w+', newline='', encoding='UTF-8')
    try:
        if lists: #列表不为空
            writer = csv.writer(csvfile)
            for i in range(len(lists)):
                writer.writerow(lists[i])
    finally:
        print('成功写入{}:{}条记录'.format(file_name, len(lists)))
        csvfile.close()


def csv_to_list(file_name, encodes='UTF-8'):
    csvfile = open(file_name, 'r', encoding=encodes)
    try:
        if csvfile.name == file_name:
            csvreader = csv.reader(csvfile)
            final_list = list(csvreader)
            return final_list
    finally:
        csvfile.close()
        print('成功读取{}条记录'.format(len(final_list)))


os.chdir('.\\data_report')
inst_city = csv_to_list('inst_city.csv')
# inst_3 = csv_to_list('inst3.csv')
inst_3 = [['340101011', '3401', '合肥市大铺头营业所'],
 ['340101012', '3401', '合肥市王大郢营业所'],
 ['340101015', '3401', '合肥市银菱营业所'],
 ['340101016', '3401', '合肥市四川路营业所'],
 ['340101017', '3401', '合肥市安庆路营业所'],
 ['340101018', '3401', '合肥市太湖东路营业所'],
 ['340101021', '3401', '合肥市华府骏苑营业所'],
 ['340101023', '3401', '合肥市黄山路营业所'],
 ['340101024', '3401', '合肥市青阳北路营业所'],
 ['340101025', '3401', '合肥市亳州路营业所'],
 ['340101028', '3401', '合肥市海恒营业所'],
 ['340101029', '3401', '合肥市三里街营业所'],
 ['340101031', '3401', '合肥市华源营业所'],
 ['340101032', '3401', '合肥市东七营业所'],
 ['340101034', '3401', '合肥市金寨南路营业所'],
 ['340101036', '3401', '合肥市潜山路营业所'],
 ['340101037', '3401', '合肥市莲花营业所'],
 ['340101038', '3401', '合肥市郎溪路营业所'],
 ['340101039', '3401', '合肥市琥珀山庄营业所'],
 ['340101040', '3401', '合肥市淝河营业所']]

res_list =[]
for item1 in inst_3:
    for item2 in inst_city:
        if (item1[1] in item2):
            cities = item2[1]
            address = ['中国邮政 ' + item1[2]]
            list_res = address_lat_lng(address, city=cities)
            list_tmp = item1 + list_res[0]
            print(list_res[0])
            res_list.append(list_tmp)
list_to_csv(res_list, 'test001.csv')

