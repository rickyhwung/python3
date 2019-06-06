import csv, json

#将列表写入csv文件（UTF-8，“,”分割）
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

#将csv文件内容读入列表（UTF-8，“,”分割）
def csv_to_list(file_name):
    csvfile = open(file_name, 'r', encoding='UTF-8')
    try:
        if csvfile.name == file_name:
            csvreader = csv.reader(csvfile)
            res_list = list(csvreader)
            return res_list
    finally:
        csvfile.close()
        print('成功读取{}条记录'.format(len(res_list)))

