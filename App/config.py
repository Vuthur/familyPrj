import socket

SERCRET_KEY = 'you_can_not_guess_the_secret_key'

# 查看是否为测试环境
if socket.gethostbyname(socket.gethostname()) == "192.168.26.1":
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:@localhost/life"
    SQLALCHEMY_POOR_SIZE = 5
    SQLALCHEMY_POOR_TIMEOUT = 10
    SQLALCHEMY_TRACK_MODIFICATIONS = False
else:
    DEBUG = False




