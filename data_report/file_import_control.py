import csv,codecs,xlwt
import os,time

# 文本文件读入列表
def txt_to_list(file_name):
    res = []
    try:
        file_open = open(file_name, 'r')
        with open(file_name, 'r') as f:
            while True:
                line = f.readline()
                if not line:
                    break
                line = line.strip('\n')
                res.append(line)
        return res
    except FileNotFoundError:
        print('文件:{}不存在，或者路径不正确。当前路径为{}'.format(file_name, os.getcwd()))
        list_to_txt(file_name, find_file())
        return res


#列表写入txt文件,覆盖模式
def list_to_txt(file_name, data):
    try:
        data = sorted(data)
        file_open = open(file_name, 'w')
        for i in range(len(data)):
            s = str(data[i]).replace('[', '').replace(']', '')  # 去除[],这两行按数据不同，可以选择
            s = s.replace("'", '').replace(',', '') + '\n'  # 去除单引号，逗号，每行末尾追加换行符
            file_open.write(s)
        file_open.close()
        print("{}\\{}文件保存成功".format(os.getcwd(), file_name))
    except FileNotFoundError:
        print('文件:{}不存在，或者路径不正确。当前路径为{}'.format(file_name, os.getcwd()))
        return None

#列表写入csv文件
def list_to_csv(file_name, data):
    file_csv = codecs.open(file_name, 'w+', 'utf-8')  # 追加
    writer = csv.writer(file_csv, delimiter=' ', quotechar=' ', quoting=csv.QUOTE_MINIMAL)
    for data in data:
        writer.writerow(data)
    print("保存文件成功，处理结束")

#列表写入excel文件
def list_to_excel(file_path, datas):
    f = xlwt.Workbook()
    sheet1 = f.add_sheet(u'sheet1', cell_overwrite_ok=True)  # 创建sheet

    # 将数据写入第 i 行，第 j 列
    i = 0
    for data in datas:
        for j in range(len(data)):
            sheet1.write(i, j, data[j])
        i = i + 1

    f.save(file_path)
    print("保存文件成功，处理结束")


# 计算列表中第n列汇总数据
def list_sum(list_name, col_num):
    res = float(0.00)
    try:
        for i in range(1, list_name.__len__()):
            res = res + float(list_name[i][col_num])
        return res
    except ValueError:
        return '第{}列不是float类型，无法统计'.format(col_num)

# 计算文件大小
def file_size(file_name):
    if os.path.exists(file_name):
        filesize = os.path.getsize(file_name)
        return filesize
    else:
        cur_path = os.getcwd()
        print('文件不存在，或者路径不正确。当前路径为{}'.format(cur_path))

# 获取文件的创建时间,比较创建、修改、访问取最早时间。
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

#返回文件创建时间的格式化字典，利用time_format()函数格式化
def file_creat_fmt(file_name, time_type='0'):
    res = time_format(file_creatime(file_name))
    if time_type == '0':
        return res
    else:
        return res[time_type]

# #检查文件名称的规范性
# def file_name_fmt(file_name):


#输入目录路径，输出最新一个符合条件的文件名
def find_new_file(dir='.\\'):
    file_lists = os.listdir(dir)
    file_lists.sort(key=lambda fn: os.path.getmtime(dir + "\\" +fn)
                    if not os.path.isdir(dir + "\\" +fn) else 0)
    list_tmp = []

    for i in file_lists:
        if not(('.txt' in i) and ('JRA' in i)):
            list_tmp.append(i)

    for j in list_tmp:
        file_lists.remove(j)

    res = file_lists[-1]
    return res

#获取当前目录符合条件文件名列表，以JRA开头的txt文件。
def find_file(dir='.\\'):
    file_lists = os.listdir(dir)
    file_lists.sort(key=lambda fn: os.path.getmtime(dir + "\\" +fn)
                    if not os.path.isdir(dir + "\\" +fn) else 0)
    list_tmp = []

    for i in file_lists:
        if not(('.txt' in i) and ('JRA' in i)):
            list_tmp.append(i)

    for j in list_tmp:
        file_lists.remove(j)

    res = file_lists
    return res

#建立当前目录下JRA*.txt文件列表，用于判断是否有新文件到来的基础，后期改为数据库表方式
def file_list_update(file_name):
    file_lists_old = txt_to_list(file_name)
    file_lists = sorted(find_file())
    if file_lists == file_lists_old:
        print('没有新文件到来')
    else:
        diffs = set(file_lists).symmetric_difference(set(file_lists_old))
        for item in diffs:
            print('有新文件：{}'.format(diffs))
        new_lists = sorted(list(set(file_lists).union(set(file_lists_old))))
        res_list = new_lists
        list_to_txt(file_name, res_list)

file_name = 'file_list.txt'
file_list_update(file_name)
#list_to_txt(file_name, find_file())