from App import api
from flask_restful import Resource

from App.CommnoModel.requestModel import Request
from App.CommnoModel.commonModel import response_form
from .familyModel import FamilyModel


class Families(Resource):
    """
    获取家人的信息列表
    """
    def __init__(self):
        self.res_data = Request().r_dict

    def get(self):
        """
        根据特征获取信息列表
        :return:
        """
        pass


class Family(Resource):
    """
    对家人信息的增删改查
    """
    def __init__(self):
        self.r_dict = Request().r_dict

    def get(self):
        """
        格局id/姓名获取具体家人的信息
        :return:
        """
        family_id = self.r_dict.get("id")
        family_name = self.r_dict.get("name")
        families = FamilyModel.family_mem(family_id, family_name)
        data = []
        for _f in families:
            data.append(_f.to_dict())
        return response_form(data)

    @staticmethod
    def post():
        """
        增添家人信息
        :return:
        """
        return

    @staticmethod
    def put():
        """
        修改家人信息
        :return:
        """
        return

    @staticmethod
    def delete():
        """删除家人信息"""
        return


api.add_resource(Families, "/family/list")
api.add_resource(Family, "/family")
