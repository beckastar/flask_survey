
from app import db
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship, scoped_session
engine = create_engine('sqlite:///bikes.db', convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))

ROLE_USER = 0
ROLE_ADMIN = 1

# @lm.user_loader
# def load_user(id):
#     return User.query.get(int(id))

Base = declarative_base()
Base.query = db_session.query_property()

#Add users later. Not necessary for MVP functionality
# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     nickname = db.Column(db.String(64), index=True, unique=True)
#     email = db.Column(db.String(120), index=True, unique=True)



#     def is_authenticated(self):
#         return True

#     def is_active(self):
#         return True

#     def is_anonymous(self):
#         return False

#     def get_id(self):
#         try:
#             return unicode(self.id)  # python 2
#         except NameError:
#             return str(self.id)  # python 3

#     def __repr__(self):
#         return '<User %r>' % (self.nickname)



class Crash_Incident(db.Model):
    __tablename__='crash_incident'
    id = db.Column(db.Integer, primary_key = True)
    cyclist_name = db.Column(db.String(15))
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

    def __repr__(self):
        return self.cyclist_name

class Road_Quality(db.Model):
    __tablename__='road_quality'
    id = db.Column(Integer, primary_key=True)
    incident_id = db.Column(Integer, ForeignKey('crash_incident.id'))
    muni_tracks = db.Column(db.Boolean)
    potholes = db.Column(db.Boolean)
    loose_materials_on_roadway = db.Column(db.Boolean)
    obstruction_on_roadway = db.Column(db.Boolean)
    construction = db.Column(db.Boolean)
    reduced_roadway_width = db.Column(db.Boolean)
    flooded = db.Column(db.Boolean)
    other_roadway_issue  = db.Column(db.String(50))

    def __repr__(self):
        return self.incident_id

class Vehicle_Violation(db.Model):
    __tablename__='vehicle_violation'
    id = db.Column(Integer, primary_key=True)
    incident_id = db.Column(Integer, ForeignKey('crash_incident.id'))
    stopped = db.Column(db.Boolean)
    driving_straight = db.Column(db.Boolean)
    ran_off_road = db.Column(db.Boolean)
    turning_right = db.Column(db.Boolean)
    turning_left = db.Column(db.Boolean)
    u_turn = db.Column(db.Boolean)
    backing_up = db.Column(db.Boolean)
    changing_lanes = db.Column(db.Boolean)
    slowing_down = db.Column(db.Boolean)
    entering_traffic = db.Column(db.Boolean)
    parking = db.Column(db.Boolean)

    def __repr__(self):
        return self.incident_id


def main():
    Base.metadata.create_all(ENGINE)


if __name__ == "__main__":
    main()
