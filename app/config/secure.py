# -*- coding:utf-8 -*-


DIALECT = 'mysql'
DRIVER = 'pymysql'
USERNAME = 'root'
PASSWORD = 'yj19930621+-*/'
HOST = '47.107.225.228'
PORT = '3306'
DATABASE = 'D-BA'
SQLALCHEMY_ENCODING = 'utf-8'
SQLALCHEMY_DATABASE_URI = "{}+{}://{}:{}@{}:{}/{}".format(DIALECT, DRIVER, USERNAME, PASSWORD, HOST,
                                                          PORT, DATABASE)
SQLALCHEMY_ECHO = False
SQLALCHEMY_TRACK_MODIFICATIONS = True

SECRET_KEY = 'DFSFSODKFPSDKFPSFKDPSOMF546546'