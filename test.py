from models.user import User
from models.topic import Topic


def add_user():
    form = dict(
        name='gua',
        password='123',
    )
    u = User.new(form)
    print('add user', u.id)


def add_topic():
    form = dict(
        title='hello',
        content='沙发',
    )
    # 可以在创建的时候给额外字段
    t = Topic.new(form, user_id=1)
    print('add topic', t)


def find_user():
    # User.get(1) 相当于 User.find_one(id=1)
    # find 是返回数组
    # User.all() 相当于 User.find()
    us = User.find(name='gua')
    print(us)


def main():
    add_user()
    find_user()


if __name__ == '__main__':
    main()
