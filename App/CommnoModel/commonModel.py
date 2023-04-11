"""
公共工具模块
"""


def response_form(data, code=200, message="Success"):
    """
    构建响应格式
    :param data:
    :param code:
    :param message:
    :return:
    """
    return {
        "result": data,
        "statusCode": code,
        "message": message
    }
