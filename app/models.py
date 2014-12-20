
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



class DateQuestions(db.Model):
    # __tablename__='survey1'
    id = db.Column(db.Integer, primary_key = True)
    injury_severity = db.Column(db.String(50))
    type_of_bike = db.Column(db.String(50))
    name_of_street = db.Column(db.String(50))
    building_address = db.Column(db.Integer)
    cross_street =db.Column(db.String(50))
    year_of_crash = db.Column(db.Integer)
    month_of_crash =db.Column(db.Integer)
    day_of_week = db.Column(db.String(10))
    approx_time = db.Column(db.Integer)
    address = db.Column(db.String(20))
    rider = db.Column(db.Boolean)
    holiday = db.Column(db.Boolean)
    road_conditions = db.Column(db.Boolean)
    vehicle_violations = db.Column(db.Boolean)
    lighting_conditions = db.Column(db.Boolean)
    road_surface = db.Column(db.Boolean)
    another_vehicle = db.Column(db.Boolean)
    other = db.Column(db.String(50))



   def __init__(self, arg):
        super(ClassName, self).__init__()
        self.arg = arg


class RoadQuality(db.Model):
    muni_tracks = db.Column(db.Boolean)
    potholes = db.Column(db.Boolean)
    loose_materials_on_roadway = db.Column(db.Boolean)
    obstruction_on_roadway = db.Column(db.Boolean)
    construction = db.Column(db.Boolean)
    reduced_roadway_width = db.Column(db.Boolean)
    flooded = db.Column(db.Boolean)
    other_roadway_issue  = db.Column(db.String(50))

class ClassName(object):
    """docstring for ClassName"""





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