"""
使用logging四大组件记录日志
"""
"""
1. 需求
现在有以下几个日志记录的需求：
    1）要求将所有级别的所有日志都写入磁盘文件中
    2）all.log 文件中记录所有的日志信息，日志格式为：日期和时间 - 日志级别 - 日志信息
    3）error.log 文件中单独记录error及以上级别的日志信息，日志格式为：日期和时间 - 日志级别 - 文件名[:行号] - 日志信息
    4）要求all.log 在每天凌晨进行日志切割

2. 分析

    1）要记录所有级别的日志，因此日志器的有效level需要设置为最低级别--DEBUG;
    2）日志需要被发送到两个不同的目的地，因此需要为日志器设置两个handler；另外，两个目的地都是磁盘文件，因此这两个handler都是与FileHandler相关的；
    3）all.log要求按照时间进行日志切割，因此他需要用logging.handlers.TimedRotatingFileHandler; 而error.log没有要求日志切割，因此可以使用FileHandler;
    4）两个日志文件的格式不同，因此需要对这两个handler分别设置格式器；
"""

import logging
import logging.handlers
import datetime

logger = logging.getLogger("mylogger")
logger.setLevel(logging.DEBUG)          # 设置最低级别的 DeBUG'

rf_handler = logging.handlers.TimedRotatingFileHandler("all.log", when="midnight", interval=1, backupCount=7, atTime= datetime.time(0, 0, 0, 0))
rf_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))    # 设置格式

f_handler = logging.FileHandler("error.log", encoding="utf-8")   # 写入日志文件
f_handler.setLevel(logging.ERROR)                # 设置日志等级
f_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(filename)s[:%(lineno)d] - %(message)s")) # 设置信息格式

logger.addHandler(rf_handler)  # 添加处理器    rf_handler
logger.addHandler(f_handler)   # 添加处理器    f_handler

logger.debug("debug message")
logger.info("info message")
logger.warning("warning message")
logger.error("error message")
logger.critical("critical message")