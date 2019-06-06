import logging
import logging.handlers
import time

format_dict = {
   1 : logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'),
   2 : logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'),
   3 : logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'),
   4 : logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'),
   5 : logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'),
   6 : logging.Formatter('%(asctime)s - %(name)s - %(levelname)s -%(pathname)s - %(lineno)d - %(message)s'),
}

# 创建一个logger
logger = logging.getLogger('mylogger')
logger.setLevel(logging.DEBUG)

myapp = logging.getLogger('myapp')
myapp.setLevel(logging.DEBUG)

# 创建一个handler，用于写入日志文件
fh = logging.FileHandler('test.log')
fh.setLevel(logging.DEBUG)

# 添加TimedRotatingFileHandler
# 定义一个1秒换一次log文件的handler
# 保留3个旧log文件
fh_date = logging.handlers.TimedRotatingFileHandler("log/myapp.log", when='S', interval=1, backupCount=3)
fh_date.setLevel(logging.DEBUG)

# 再创建一个handler，用于输出到控制台
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

# 定义handler的输出格式
formatter = format_dict[6]
fh.setFormatter(formatter)
fh_date.setFormatter(formatter)
ch.setFormatter(formatter)

# 给logger添加handler
logger.addHandler(fh)
logger.addHandler(ch)
myapp.addHandler(fh_date)
# logger.addHandler(fh_date)

# 记录一条日志
while True:
    time.sleep(0.1)
    myapp.info("test")
    logger.info('foorbar')