# -*- coding:utf-8 -*-
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired, length, Email, Regexp, ValidationError

from app.libs.enums import ClientTypeEnum
from app.models.user import User
from app.validators.base import BaseForm as Form


class ClientForm(Form):
    account = StringField(validators=[DataRequired(message='不允许为空'), length(min=5, max=32)])
    secret = StringField()
    type = IntegerField(validators=[DataRequired()])

    def validate_type(self, value):
        try:
            client = ClientTypeEnum(value.data)
        except ValueError as e:
            raise e
        self.type.data = client


class UserEmailForm(ClientForm):
    account = StringField(validators=[
        Email(message='invalidate email')
    ])
    secret = StringField(validators=[
        DataRequired(),
        Regexp(r'^[A-Za-z0-9_*&$#@]{6,22}$')
    ])

    nickname = StringField(validators=[DataRequired(),
                                       length(min=2, max=22)])

    # validate_字段名(self,value)  自定义验证
    def validate_account(self, value):
        # self.data 当前传过来的所有值 {'type': <ClientTypeEnum.USER_EMAIL: 100>, 'account': '66116@qq.com', 'secret': '123456', 'nickname': 'jyfan5g'}
        # self.value 当前验证的值
        if User.query.filter_by(email=value.data).first():
            raise ValidationError("邮箱号已经存在")

    def validate_nickname(self, value):
        if User.query.filter_by(nickname=value.data).first():
            raise ValidationError("昵称已经存在")

