from flask_restful import Resource
from App import app, api


class UserCtr(Resource):

    @staticmethod
    def get():
        return "hello"

    @staticmethod
    def post():
        return

    @staticmethod
    def put():
        return


api.add_resource(UserCtr, "/user")

