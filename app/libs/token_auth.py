# -*- coding:utf-8 -*-
from flask_httpauth import HTTPBasicAuth

auth = HTTPBasicAuth()


@auth.verify_password
def verify_password(account, password):
    print(account,password)
    return True
