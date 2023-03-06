from flask import request, g
from App import app


class Request:
    def __init__(self):
        self.r_dict = {}
        self.request_form()

    # @staticmethod
    # @app.before_request
    def request_form(self):
        """
        获取请求体或请求头的信息
        :return:
        """
        if request.args:
            self.r_dict = request.args
        elif request.form:
            self.r_dict = request.form
        elif request.json:
            self.r_dict = request.json
        elif request.data:
            self.r_dict = request.data
        return

    @staticmethod
    @app.after_request
    def request_info_deal(res):
        g.value = 1
        return res

    @staticmethod
    @app.teardown_request
    def request_error(res):
        """
        处理请求错误的信息，并记录日志
        :return:
        """
        if hasattr(g, "value") and g.value == 1:
            pass
        return res





