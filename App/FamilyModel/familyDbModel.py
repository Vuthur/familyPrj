import time

from App import db


class Family(db.Model):
    __tablename__ = "family"

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_id = db.Column(db.Integer, comment='创建者id')
    is_public = db.Column(db.Integer, comment="是否公有，默认私有0")
    name = db.Column(db.String(30), index=True, comment='家人名称')
    birthday = db.Column(db.Integer, comment="家人生日")
    tel_num = db.Column(db.BigInteger, unique=True, comment="电话号码")
    address = db.Column(db.String(500), comment="现住址")
    interests = db.Column(db.String(500), comment='兴趣爱好')
    imp_date = db.Column(db.String(500), comment="其他重要日期")
    is_delete = db.Column(db.Integer, index=True, comment="是否删除")
    is_china_date = db.Column(db.Integer, comment="是否是农历生日")
    create_time = db.Column(db.Integer, index=True, comment='创建时间')
    update_time = db.Column(db.Integer, comment='更新时间')

    # user = db.relationship('User', backref='families')

    def __init__(self):
        self.create_time = int(time.time())
        self.is_china_date = 0
        self.is_public = 0

    def __repr__(self):
        return "<Family: %s-%d>" % (self.name, self.id)

    def to_dict(self):
        return {
            "id": self.id,
            "uer_id": self.user_id,
            "is_public": self.is_public,
            "name": self.name,
            "birthday": self.birthday,
            "tel_num": self.tel_num,
            "address": self.address,
            "interests": self.interests,
            "imp_date": self.imp_date,
            "is_delete": self.is_delete,
            "is_china_date": self.is_china_date,
            "create_time": self.create_time,
            "update_time": self.update_time,
        }
