# -*- coding:utf-8 -*-
from app.libs.redprint import RedPrint
from app.libs.token_auth import auth
api = RedPrint('user')


@api.route('/get')
@auth.login_required
def get_user():
    return 'this user'

