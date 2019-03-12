# -*- coding:utf-8 -*-
from app.libs.error_code import DeleteSuccess, AuthFailed
from app.libs.redprint import RedPrint
from app.libs.token_auth import auth
from app.models.base import db
from app.models.user import User
from flask import jsonify, g

api = RedPrint('user')


@api.route('/<int:uid>', methods=['GET'])
def super_get_user(uid):
    is_admin = g.user.is_admin
    user = User.query.filter_by(id=uid).first_or_404()
    if not is_admin:
        raise AuthFailed()
    return jsonify(user)


@api.route('', methods=['GET'])
@auth.login_required
def get_user():
    uid = g.user.uid
    user = User.query.filter_by(id=uid).first_or_404()
    return jsonify(user)


@api.route('', methods=['DELETE'])
@auth.login_required
def delete_user():
    uid = g.user.uid
    with db.auto_commit():
        user = User.query.filter_by(id=uid).first_or_404()
        user.delete()
    return DeleteSuccess()
