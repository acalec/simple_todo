from models.forms import LoginForm
from models.user import User
from routes import *

main = Blueprint('user', __name__)

Model = User


@main.route('/')
def index():
    u = current_user
    print("u", u)
    ms = Model.all()
    return render_template('user/login.html', user_list=ms)


@main.route('/add', methods=['POST'])
def add():
    form = request.form
    print("form1", form)
    Model.new(form)
    return redirect(url_for('todo.index'))


@main.route('/login', methods=['GET', 'POST'])
def login():
    # form = request.form
    form = LoginForm()
    print("form",  form.username.data)
    user = User.find_one(username=form.username.data)

    if form.validate_on_submit() and user.validate_auth(form):
        print('Logged in successfully.')
        return redirect(url_for('todo.index'))
    else:
        print('Invalid username or password')
    return render_template('user/login.html', form=form)
