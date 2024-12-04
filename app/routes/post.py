from flask import Blueprint
from ..extensions import DB
from ..models.post import Post

POST = Blueprint('post', __name__)

@POST.route('/post/<subject>')
def create_user(subject):
    post = Post(subject=subject)
    DB.session.add(post)
    DB.session.commit()
    return 'Subject created successfully!'
