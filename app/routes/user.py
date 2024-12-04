from flask import Blueprint
from ..extensions import DB
from ..models.user import User

USER = Blueprint('user', __name__)

@USER.route('/user/<name>')
def create_user(name):
    user = User(name=name)
    DB.session.add(user)
    DB.session.commit()
    return 'User created successfully!'