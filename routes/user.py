from models.user import User
from routes import *
from models.forms import LoginForm

main = Blueprint('user', __name__)

Model = User


@main.route('/')
def index():
    u = current_user
    print("u", u)
    # if u is not None:
    #     return redirect(url_for('todo.index'))
    ms = Model.all()
    return render_template('user/index.html', user_list=ms)


@main.route('/add', methods=['POST'])
def add():
    form = request.form
    # u = Model(form)
    print("form1", form)
    Model.new(form)
    return redirect(url_for('todo.index'))


@main.route('/login', methods=['GET', 'POST'])
def login():
    # form = request.form
    form = LoginForm()
    print("form", form['username'], form)
    user = Model.find_one(username=form['username'])
    print("user",user)
    if user:
        # Login and validate the user.
        # user should be an instance of your `User` class
        user = current_user
        login_user(user)
        flash('Logged in successfully.')
        return redirect(url_for('todo.index'))
    else:
        flash('Invalid username or password')
    return render_template('user/index.html', form=form)
