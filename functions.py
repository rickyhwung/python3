import csv, json, os, sys, time

#将列表写入csv文件（UTF-8，“,”分割）
def list_to_csv(lists, file_name):
    with open(file_name, 'w+', newline='', encoding='UTF-8') as csvfile:
        try:
            if lists: #列表不为空
                writer = csv.writer(csvfile)
                for i in range(len(lists)):
                    writer.writerow(lists[i])
        except csv.Error as e:
            sys.exit('file {}, line {}: {}'.format(file_name, writer.line_num, e))
        finally:
            print('成功写入{}:{}条记录'.format(file_name, len(lists)))
            csvfile.close()

#将csv文件内容读入列表（UTF-8，“,”分割）
def csv_to_list(file_name):
    with open(file_name, newline='', encoding='UTF-8') as csvfile:
        csvreader = csv.reader(csvfile)
        try:
            if csvfile.name == file_name:
                res_list = list(csvreader)
        except csv.Error as e:
            sys.exit('file {}, line {}: {}'.format(file_name, csvreader.line_num, e))
        finally:
            if res_list == []:
                print('文件记录为空')
            else:
                for item in res_list:
                    for j in range(len(item)):
                        item[j] = item[j].strip()
                return res_list
                print('成功读取{}条记录'.format(len(res_list)))
            csvfile.close()

#返回YYYYMMDD、HHMMSS格式时间字符串
def time_to_str(input_time, res_type='hms'):
    if res_type == 'ymd':
        res_time = time.strftime("%Y%m%d", time.localtime(input_time))
        return res_time
    elif res_type == 'hms':
        res_time = time.strftime("%H%M%S", time.localtime(input_time))
        return res_time
    elif res_type == 'ymdhms':
        res_time = time.strftime("%Y%m%d%H%M%S", time.localtime(input_time))
        return res_time
    else:
        res_time = time.strftime("%Y%m%d%H%M%S", time.localtime(time.time()))
        return res_time

# 计算文件大小
def file_size(file_name):
    if os.path.exists(file_name):
        filesize = os.path.getsize(file_name)
        return filesize
    else:
        cur_path = os.getcwd()
        print('文件不存在，或者路径不正确。当前路径为{}'.format(cur_path))

