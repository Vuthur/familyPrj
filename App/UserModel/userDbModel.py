import time

from App import db


class User(db.Model):
    __tablename__ = "user"

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String(30), index=True, comment='姓名/昵称/爱称')
    passwd = db.Column(db.String(50), comment="账号密码")
    birthday = db.Column(db.Integer, comment="你的生日")
    address = db.Column(db.String(200), comment="现住址")
    tel_num = db.Colum(db.BigInteger, unique=True, comment="电话号码")
    wechat_num = db.Column(db.String(50), comment="微信号")
    email = db.Column(db.String(50), comment="邮箱地址")
    is_delete = db.Column(db.Integer, index=True, comment="是否删除")
    is_china_date = db.Column(db.Integer, comment="是否是农历生日")
    create_time = db.Column(db.Integer, index=True, comment='创建时间')
    update_time = db.Column(db.Integer, comment='更新时间')

    def __init__(self):
        self.create_time = int(time.time())
        self.is_china_date = 0

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "birthday": self.birthday,
            "address": self.address,
            "tel_num": self.tel_num,
            "wechat_num": self.wechat_num,
            "email": self.email,
            "is_delete": self.is_delete,
            "is_china_date": self.is_china_date,
            "create_time": self.create_time,
            "update_time": self.update_time,
        }
