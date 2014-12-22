
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

class User(db.Model):
    __tablename__="user"
    cyclist_name = db.Column(db.String(15))
    cyclist_email = db.Column(db.String(25))
    cyclist_age= db.Column(db.Integer)




class Crash_Incident(db.Model):
    __tablename__='crash_incident'
    id = db.Column(db.Integer, primary_key = True)
    injury_severity = db.Column(db.String(50))
    type_of_bike = db.Column(db.String(50))
    name_of_street = db.Column(db.String(50))
    building_address = db.Column(db.Integer)
    cross_street =db.Column(db.String(50))
    year_of_crash = db.Column(db.Integer, default = 2015)
    month_of_crash =db.Column(db.Integer)
    day_of_week = db.Column(db.String(10))
    approx_time = db.Column(db.Integer)
    rider = db.Column(db.Boolean, default=True)
    holiday = db.Column(db.Boolean, default = False)
    road_conditions = db.Column(db.Boolean, default= False)
    vehicle_violations = db.Column(db.Boolean, default = False)
    lighting_conditions = db.Column(db.Boolean, default= False)
    road_surface = db.Column(db.Boolean, default=False)
    another_vehicle = db.Column(db.Boolean, default=True)
    other = db.Column(db.String(50))

    def __init__(self, cyclist_name, injury_severity, type_of_bike, name_of_street, building_address, cross_street, year_of_crash, month_of_crash, day_of_week, approx_time, rider, holiday, road_conditions, vehicle_violations, lighting_conditions, road_surface, another_vehicle, other)
        self.cyclist_name = cyclist_name
        self.injury_severity = injury_severity
        self.type_of_bike = type_of_bike
        self.name_of_street = name_of_street
        self.building_address = building_address
        self.cross_street = cross_street
        self.year_of_crash = year_of_crash
        self.month_of_crash = month_of_crash
        self.day_of_week = day_of_week
        self.approx_time = approx_time
        self.rider = rider
        self.holiday = holiday
        self.road_conditions = road_conditions
        self.vehicle_violations = vehicle_violations
        self.lighting_conditions = lighting_conditions
        self.road_surface = road_surface
        self.another_vehicle = another_vehicle
        self.other = other

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

class Other_Vehicle(db.Model):
    __tablename__='other_vehicle'
    id = db.Column(Integer, primary_key=True)
    incident_id = db.Column(Integer, ForeignKey('crash_incident.id'))
    bike =db.Column(db.Boolean, default = False)
    car = db.Column(db.Boolean, default = False)
    motorcycle = db.Column(db.Boolean, default = False)
    bus = db.Column(db.Boolean, default = False)
    muni = db.Column(db.Boolean, default = False)


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
