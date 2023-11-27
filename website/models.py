from . import db
from flask_login import UserMixin


class User(db.Model, UserMixin):
    pass


#min 1:17:52