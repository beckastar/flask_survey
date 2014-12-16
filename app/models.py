
from app import db

ROLE_USER = 0
ROLE_ADMIN = 1

# @lm.user_loader
# def load_user(id):
#     return User.query.get(int(id))


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nickname = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    posts = db.relationship('Post', backref='author', lazy='dynamic')

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.id)  # python 2
        except NameError:
            return str(self.id)  # python 3

    def __repr__(self):
        return '<User %r>' % (self.nickname)


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Post %r>' % (self.body)

class Survey1(db.Model):
    # __tablename__='survey1'
    id = db.Column(db.Integer, primary_key = True)
    incident = db.Column(db.String(50))
    address = db.Column(db.String(50))
    rider = db.Column(db.Boolean)




    #user = db.relationship('User', backref=db.backref('survey1', lazy='dynamic'))

    def __init__(self, gender=None,age=None):
        self.userid = userid

    def get_id(self):
        return unicode(self.id)


class Survey2(db.Model):
    # __tablename__='survey2'
    id = db.Column(db.Integer, primary_key = True)
    userid = db.Column(db.String(255))
    def __init__(self, major=None, department=None, count=None, unique=None, userid=None):
        self.major=major
        # self.department=department
        self.count=count
        self.unique=unique
        self.userid=userid

    def get_id(self):
        return unicode(self.id)

    def get_id(self):
        return unicode(self.id)