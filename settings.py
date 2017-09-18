#coding:utf-8

##数据库配置
MONGO_HOST = 'localhost'
MONGO_PORT = 27017
MONGO_DB = 'edu'
MONGO_URI = 'mongodb://{HOST}:{PORT}/{DB}'.format(HOST=MONGO_HOST,PORT=MONGO_PORT,DB=MONGO_DB)

#http相应状态码
CODE = {
    'OK': 200,
    'created': 201,
    'no-content': 204,
    'not-found': 404
}

#pre_fix = '/api/v1'
