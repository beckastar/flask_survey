from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
RoadQuality = Table('RoadQuality', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('incident_id', INTEGER),
    Column('muni_tracks', BOOLEAN),
    Column('potholes', BOOLEAN),
    Column('loose_materials_on_roadway', BOOLEAN),
    Column('obstruction_on_roadway', BOOLEAN),
    Column('construction', BOOLEAN),
    Column('reduced_roadway_width', BOOLEAN),
    Column('flooded', BOOLEAN),
    Column('other_roadway_issue', VARCHAR(length=50)),
)

VehicleViolation = Table('VehicleViolation', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('stopped', BOOLEAN),
    Column('driving_straight', BOOLEAN),
    Column('ran_off_road', BOOLEAN),
    Column('turning_right', BOOLEAN),
    Column('turning_left', BOOLEAN),
    Column('u_turn', BOOLEAN),
    Column('backing_up', BOOLEAN),
    Column('changing_lanes', BOOLEAN),
    Column('slowing_down', BOOLEAN),
    Column('entering_traffic', BOOLEAN),
    Column('parking', BOOLEAN),
)

road_quality = Table('road_quality', post_meta,
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

vehicle_violation = Table('vehicle_violation', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('incident_id', Integer),
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


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['RoadQuality'].drop()
    pre_meta.tables['VehicleViolation'].drop()
    post_meta.tables['road_quality'].create()
    post_meta.tables['vehicle_violation'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['RoadQuality'].create()
    pre_meta.tables['VehicleViolation'].create()
    post_meta.tables['road_quality'].drop()
    post_meta.tables['vehicle_violation'].drop()
