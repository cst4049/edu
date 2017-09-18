#coding: utf-8
from flask import Flask, request
from flask_restful import Api, Resource
from flask_pymongo import PyMongo
from settings import MONGO_URI
from model import BokT,BotT


app = Flask(__name__)

app.config['MONGO_URI'] = MONGO_URI

api = Api(app)
mongo = PyMongo(app)


class TitleList(Resource):
    '''
    题库操作
    '''
    def get(self):
        '获取题目列表'
        titles = mongo.db.titles.find({},{"_id":0})
        title_list = list(titles)
        return dict(result='success', titlelist=title_list)

    def post(self):
        '''新增题目'''
        title = request.get_json()
        if isinstance(title,dict):
            title_id = mongo.db.titles.insert_one(title).inserted_id
        if isinstance(title,list):
            title_id = mongo.db.titles.insert(title)
        if title_id is not None:
            return dict(result='success', message='record added')
        return dict(result='error', message='Failed to insert')


class Title(Resource):
    '''
    对单个题目的操作
    '''
    def get(self, name):
        '''获取指定题目'''
        title = mongo.db.titles.find_one({'name': name},{"_id":0})
        if title is not None:
            return dict(result='success', title=title)
        return dict(result='error', message='No record found')

    def delete(self, name):
        '''删除指定题目'''
        result = mongo.db.title.delete_one({'name': name})
        count = result.deleted_count
        if count > 0:
            return dict(result='success', message='%d records deleted' % count)
        return dict(result='error', message='Failed to delete')

    def put(self, name):
        '''修改指定的题目'''
        title = request.get_json()
        result = mongo.db.titles.replace_one({'name': 'name'}, title)
        count = result.modified_count
        if count > 0:
            return dict(result='success', message='%d records modified' % count)
        return dict(result='error', message='Failed to modify')


class BokList(Resource):
    '''
    知识库操作
    '''
    def get(self):
        '获取知识库列表'
        boks = mongo.db.boks.find({},{"_id":0}).paginate(page="page",per_page=10)
        bok_list = list(boks)
        return dict(result='success', boklist=bok_list)

    def post(self):
        '''新增知识库内容'''
        bok = request.get_json()
        if isinstance(bok,dict):
            bokt = BokT(**bok)
            bokt_attr = bokt.__dict__
            bok_id = mongo.db.boks.insert_one(bokt_attr).inserted_id
        if isinstance(bok,list):
            bokt_attr = [BokT(**i).__dict__ for i in bok]
            bok_id = mongo.db.boks.insert(bokt_attr)
        if bok_id is not None:
            return dict(result='success', message='record added')
        return dict(result='error', message='Failed to insert')


class Bok(Resource):
    '''
    对单个知识点的操作
    '''
    def get(self, name):
        '''获取指定知识点'''
        bok = mongo.db.boks.find_one({'root': name},{"_id":0})
        if bok is not None:
            return dict(result='success', bok=bok)
        return dict(result='error', message='No record found')

    def delete(self, name):
        '''删除指定知识点'''
        result = mongo.db.boks.delete_one({'root': name})
        count = result.deleted_count
        if count > 0:
            return dict(result='success', message='%d records deleted' % count)
        return dict(result='error', message='Failed to delete')

    def put(self, name):
        '''修改指定的知识点'''
        bok = request.get_json()
        result = mongo.db.boks.replace_one({'root': 'name'}, bok)
        count = result.modified_count
        if count > 0:
            return dict(result='success', message='%d records modified' % count)
        return dict(result='error', message='Failed to modify')


class BotList(Resource):
    '''
    章节体操作
    '''
    def get(self):
        '获取章节体列表'
        bots = mongo.db.bots.find({},{"_id":0})
        bot_list = list(bots)
        return dict(result='success', botlist=bot_list)

    def post(self):
        '''新增章节体内容'''
        bot = request.get_json()
        if isinstance(bot,dict):
            bott = BotT(**bot)
            bott_attr = bott.__dict__
            bot_id = mongo.db.bots.insert_one(bott_attr).inserted_id
        if isinstance(bot,list):
            bott_attr = [BotT(**i).__dict__ for i in bot]
            bot_id = mongo.db.bots.insert(bott_attr)
        if bot_id is not None:
            return dict(result='success', message='record added')
        return dict(result='error', message='Failed to insert')


class Bot(Resource):
    '''
    对单个章节的操作
    '''
    def get(self, name):
        '''获取指定章节'''
        bot = mongo.db.bots.find_one({'root': name},{"_id":0})
        if bot is not None:
            return dict(result='success', bot=bot)
        return dict(result='error', message='No record found')

    def delete(self, name):
        '''删除指定章节'''
        result = mongo.db.bots.delete_one({'root': name})
        count = result.deleted_count
        if count > 0:
            return dict(result='success', message='%d records deleted' % count)
        return dict(result='error', message='Failed to delete')

    def put(self, name):
        '''修改指定的章节'''
        bot = request.get_json()
        result = mongo.db.bots.replace_one({'root': 'name'}, bot)
        count = result.modified_count
        if count > 0:
            return dict(result='success', message='%d records modified' % count)
        return dict(result='error', message='Failed to modify')


api.add_resource(TitleList, '/titles/')
api.add_resource(Title, '/titles/<name>/')

api.add_resource(BokList, '/boks/')
api.add_resource(Bok, '/boks/<name>/')

api.add_resource(BotList, '/bots/')
api.add_resource(Bot, '/bots/<name>/')