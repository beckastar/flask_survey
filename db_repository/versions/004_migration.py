from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
post = Table('post', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('body', VARCHAR(length=140)),
    Column('timestamp', DATETIME),
    Column('user_id', INTEGER),
)

survey1 = Table('survey1', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('incident', VARCHAR(length=50)),
    Column('address', VARCHAR(length=50)),
    Column('rider', BOOLEAN),
)

survey2 = Table('survey2', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('userid', VARCHAR(length=255)),
)

RoadQuality = Table('RoadQuality', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('incident_id', Integer),
    Column('muni_tracks', Boolean),
    Column('potholes', Boolean),
    Column('loose_materials_on_roadway', Boolean),
    Column('obstruction_on_roadway', Boolean),
    Column('construction', Boolean),
    Column('reduced_roadway_width', Boolean),
    Column('flooded', Boolean),
    Column('other_roadway_issue', String(length=50)),
)

VehicleViolation = Table('VehicleViolation', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('stopped', Boolean),
    Column('driving_straight', Boolean),
    Column('ran_off_road', Boolean),
    Column('turning_right', Boolean),
    Column('turning_left', Boolean),
    Column('u_turn', Boolean),
    Column('backing_up', Boolean),
    Column('changing_lanes', Boolean),
    Column('slowing_down', Boolean),
    Column('entering_traffic', Boolean),
    Column('parking', Boolean),
)

crash_incident = Table('crash_incident', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('injury_severity', String(length=50)),
    Column('type_of_bike', String(length=50)),
    Column('name_of_street', String(length=50)),
    Column('building_address', Integer),
    Column('cross_street', String(length=50)),
    Column('year_of_crash', Integer),
    Column('month_of_crash', Integer),
    Column('day_of_week', String(length=10)),
    Column('approx_time', Integer),
    Column('address', String(length=20)),
    Column('rider', Boolean),
    Column('holiday', Boolean),
    Column('road_conditions', Boolean),
    Column('vehicle_violations', Boolean),
    Column('lighting_conditions', Boolean),
    Column('road_surface', Boolean),
    Column('another_vehicle', Boolean),
    Column('other', String(length=50)),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['post'].drop()
    pre_meta.tables['survey1'].drop()
    pre_meta.tables['survey2'].drop()
    post_meta.tables['RoadQuality'].create()
    post_meta.tables['VehicleViolation'].create()
    post_meta.tables['crash_incident'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['post'].create()
    pre_meta.tables['survey1'].create()
    pre_meta.tables['survey2'].create()
    post_meta.tables['RoadQuality'].drop()
    post_meta.tables['VehicleViolation'].drop()
    post_meta.tables['crash_incident'].drop()
