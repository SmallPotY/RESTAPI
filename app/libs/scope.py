# -*- coding:utf-8 -*-


class AdminScope:
    allow_api = ['v1.super_get_user']


class UserScope:
    allow_api = []


def is_in_scope(scope, endpoint):
    # globals()[scope]()   根据类名动态创建类对象
    scope = globals()[scope]()
    if endpoint in scope.allow_api:
        return True
    else:
        return False
