import csv
import os,time

# 文本文件读入列表
def txt_to_list(file_name):
    file_open = open(file_name, 'r')
    csvreader = csv.reader(file_open)
    final_list = list(csvreader)
    return final_list

# 计算列表中第n列汇总数据
def list_sum(list_name, col_num):
    res = float(0)
    for i in range(1, list_name.__len__()):
        res = res + float(list_name[i][col_num])
    return res

# 计算文件大小
def file_size(file_name):
    if os.path.exists(file_name):
        filesize = os.path.getsize(file_name)
        return filesize
    else:
        cur_path = os.getcwd()
        return '文件不存在，或者路径不正确。当前路径为{}'.format(cur_path)

# 获取文件的创建时间
def file_creatime(file_name):
    creat_time_m = os.path.getmtime(file_name)
    creat_time_a = os.path.getatime(file_name)
    creat_time_c = os.path.getctime(file_name)
    creat_time = min(creat_time_a, creat_time_c, creat_time_m)
    return creat_time


#时间time类型格式化，返回字典｛fmt_year,fmt_mon,fmt_day,fmt_hour,fmt_min,fmt_sec}
def time_format(input_time):
    fmt_time = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(input_time))
    res_time = {'fmt_year': fmt_time[0:4],
                'fmt_mon': fmt_time[5:7],
                'fmt_day': fmt_time[8:10],
                'fmt_hour': fmt_time[11:13],
                'fmt_min': fmt_time[14:16],
                'fmt_sec': fmt_time[17:19],
                }
    return res_time

#返回文件创建时间的格式化字典
def file_creat_fmt(file_name, time_type='0'):
    res = time_format(file_creatime(file_name))
    if time_type == '0':
        return res
    else:
        return res[time_type]

#检查文件名称的规范性
def file_name_fmt(file_name):


#输入目录路径，输出最新文件名
def find_new_file(dir='.\\'):
    file_lists = os.listdir(dir)
    file_lists.sort(key=lambda fn: os.path.getmtime(dir + "\\" +fn)
                    if not os.path.isdir(dir + "\\" +fn) else 0)
    list_tmp = []

    for i in file_lists:
        if not('txt' in i):
            list_tmp.append(i)

    for j in list_tmp:
        file_lists.remove(j)

    res = file_lists[-1]
    return res
