#-*- coding: utf-8 -*-

__author__ = '打补丁的狮子'


import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename='myapp.log',
                    filemode='w')

#定义一个StreamHandler, 将INFO级别或更高的日志信息打印到标准错误，并将其添加到当前的日志处理对象
console = logging.StreamHandler()
console.setLevel(logging.INFO)
formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
console.setFormatter(formatter)
logging.getLogger('').addHandler(console)

logging.debug('This is debug message')
logging.info('This is info message')
logging.warning('This is warning message')


#日志回滚
from logging.handlers import RotatingFileHandler

#定义一个RotatingFileHandler,最多备份5个日志文件，每个日志文件最大10M
rthandler = RotatingFileHandler('rlog.log', maxBytes=10*1024*1024, backupCount=5)
rthandler.setLevel(logging.INFO)
formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
rthandler.setFormatter(formatter)
logging.getLogger('').addHandler(rthandler)

#通过配置文件配置日志打印
import logging.config

logging.config.fileConfig("logger.conf")
logger = logging.getLogger("example01")

logger.debug('This is debug message')
logger.info('This is info message')
logger.warning('This is warning message')

logger = logging.getLogger("example02")

logger.debug('This is debug message')
logger.info('This is info message')
logger.warning('This is warning message')