import json

from models.todo import Todo
from routes import *
from flask_login import login_required

main = Blueprint('todo', __name__)

Model = Todo


def api_response(success, data=None, message=''):
    r = {
        'success': success,
        'data': data,
        'message': message,
    }
    return json.dumps(r, ensure_ascii=False)


@main.route('/')
@login_required
def index():
    ms = Model.find()
    if ms is None:
        ms = []
    print("ms", ms)
    return render_template('todo/todo_index.html', todo_list=ms)


@main.route('/add', methods=['POST'])
def add():
    form = request.form
    Model.insert(form)
    return redirect(url_for('.index'))


@main.route('/edit/<id>')
def edit(id):
    m = Model.find_by_id(id)
    print("m", m)
    return render_template('todo/todo_edit.html', todo=m)


@main.route('/update/<id>', methods=['POST'])
def update(id):
    form = request.form
    m = Model.update(id, form)
    return redirect(url_for('todo.index'))


@main.route('/delete/<id>')
def delete(id):
    Model.delete(id)
    return redirect(url_for('.index'))
