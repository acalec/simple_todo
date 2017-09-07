from flask import Flask
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager


from models import db
from models.todo import Todo
from models.user import User


app = Flask(__name__)
manager = Manager(app)


def configured_app():
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    import config
    app.secret_key = config.secret_key
    app.config['SQLALCHEMY_DATABASE_URI'] = config.db_uri
    db.init_app(app)
    register_routes(app)
    configure_log(app)
    return app


def configure_log(app):
    if not app.debug:
        import logging
        stream_handler = logging.StreamHandler()
        stream_handler.setLevel(logging.INFO)
        app.logger.addHandler(stream_handler)


def configure_manager():
    Migrate(app, db)
    manager.add_command('db', MigrateCommand)


def register_routes(app):
    from routes.todo import main as routes_todo
    app.register_blueprint(routes_todo, url_prefix='/todo')

    from routes.user import main as routes_user
    app.register_blueprint(routes_user, url_prefix='/user')


@manager.command
def server():
    """
    用原始的方法启动程序
    """
    app = configured_app()
    config = dict(
        debug=True,
        host='127.0.0.1',
        port=3000,
    )
    app.run(**config)


if __name__ == '__main__':
    configure_manager()
    configured_app()
    manager.run()
