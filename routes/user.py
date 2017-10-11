from models.forms import LoginForm
from models.user import User
from routes import *
main = Blueprint('user', __name__)

Model = User


@main.route('/add', methods=['POST'])
def add():
    form = request.form
    print("form1", form)
    Model.new(form)
    return redirect(url_for('todo.index'))


@main.route('/', methods=['GET', 'POST'])
def login():
    # form = request.form
    form = LoginForm()
    print("form", form.username.data)
    user = User.find_one(username=form.username.data)
    if user is not None:
        if form.validate_on_submit() and user.validate_auth(form):
            login_user(user, remember=True)

            print('Logged in successfully.', current_user, current_user.is_authenticated)
            next = request.args.get('next')
            return redirect(url_for(next or 'todo.index'))
        else:
            print('Invalid username or password')
    return render_template('user/login.html', form=form)
