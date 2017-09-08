# from models.forms import LoginForm
from models.user import is_safe_url
from . import *

main = Blueprint('login', __name__)


