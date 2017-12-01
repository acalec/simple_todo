import time

import pymongo
from bson.objectid import ObjectId

# from . import db

client = pymongo.MongoClient("mongodb://localhost:27017")
print('连接数据库成功', client)

mongodb_name = 'todo_demo'
db = client[mongodb_name]


class Todo(object):
    def __init__(self, form):
        self.name = form.get('name', '')

        self.created_time = int(time.time())
        self.update_time = int(time.time())

    @classmethod
    def insert(cls, form,final_num):
        u = {
            'name': form.get('name', ''),
            'reason': form.get('reason', ''),
            'count': form.get('count', ''),
            'maxx': form.get('maxx', ''),
            'revise': form.get('revise', ''),
            'final_num': final_num,
            'created_time': int(time.time()),
            'updated_time': int(time.time()),
        }
        db.todo_demo.insert(u)

    @classmethod
    def update(cls, id, form):
        q = {
            "_id": ObjectId(id)
        }
        u = {
            'task': form.get('task', ''),
        }
        f = {
            '$set': u
        }
        options = {
            'multi': True,
        }
        db.todo_demo.update(q, f, **options)

    @classmethod
    def find_by_id(cls, id):
        query = {
            "_id": ObjectId(id)
        }
        a = db.todo_demo.find_one(query)

        return a

    @staticmethod
    def find():
        todo_list = list(db.todo_demo.find())
        # print('find all', todo_list)
        return todo_list

    @classmethod
    def delete(cls, id):
        query = {
            "_id": ObjectId(id)
        }
        db.todo_demo.remove(query)

    def get_created_time(self):
        format = '%Y-%m-%d %H:%M'
        value = time.localtime(int(self.created_time))
        dt = time.strftime(format, value)
        return dt


def format_time(value):
    format = '%Y-%m-%d %H:%M'
    value = time.localtime(value)
    dt = time.strftime(format, value)
    return dt