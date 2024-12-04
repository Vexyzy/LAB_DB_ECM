from datetime import datetime

from ..extensions import DB

class Post(DB.Model):
    id = DB.Column(DB.Integer, primary_key=True)
    subject = DB.Column(DB.String(255), nullable=False)
    teacher = DB.Column(DB.String(255), nullable=False)
    student = DB.Column(DB.String(255), nullable=False)
    date = DB.Column(DB.DateTime, nullable=False, default=datetime.now())


