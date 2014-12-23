from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
other_vehicle = Table('other_vehicle', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('incident_id', Integer),
    Column('bike', Boolean, default=ColumnDefault(False)),
    Column('car', Boolean, default=ColumnDefault(False)),
    Column('motorcycle', Boolean, default=ColumnDefault(False)),
    Column('bus', Boolean, default=ColumnDefault(False)),
    Column('muni', Boolean, default=ColumnDefault(False)),
)

crash_incident = Table('crash_incident', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('injury_severity', VARCHAR(length=50)),
    Column('type_of_bike', VARCHAR(length=50)),
    Column('name_of_street', VARCHAR(length=50)),
    Column('building_address', INTEGER),
    Column('cross_street', VARCHAR(length=50)),
    Column('year_of_crash', INTEGER),
    Column('month_of_crash', INTEGER),
    Column('day_of_week', VARCHAR(length=10)),
    Column('approx_time', INTEGER),
    Column('address', VARCHAR(length=20)),
    Column('rider', BOOLEAN),
    Column('holiday', BOOLEAN),
    Column('road_conditions', BOOLEAN),
    Column('vehicle_violations', BOOLEAN),
    Column('lighting_conditions', BOOLEAN),
    Column('road_surface', BOOLEAN),
    Column('another_vehicle', BOOLEAN),
    Column('other', VARCHAR(length=50)),
)

user = Table('user', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('nickname', VARCHAR(length=64)),
    Column('email', VARCHAR(length=120)),
)

user = Table('user', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('cyclist_name', String(length=15)),
    Column('cyclist_email', String(length=25)),
    Column('cyclist_age', Integer),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['other_vehicle'].create()
    pre_meta.tables['crash_incident'].columns['address'].drop()
    pre_meta.tables['user'].columns['email'].drop()
    pre_meta.tables['user'].columns['nickname'].drop()
    post_meta.tables['user'].columns['cyclist_age'].create()
    post_meta.tables['user'].columns['cyclist_email'].create()
    post_meta.tables['user'].columns['cyclist_name'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['other_vehicle'].drop()
    pre_meta.tables['crash_incident'].columns['address'].create()
    pre_meta.tables['user'].columns['email'].create()
    pre_meta.tables['user'].columns['nickname'].create()
    post_meta.tables['user'].columns['cyclist_age'].drop()
    post_meta.tables['user'].columns['cyclist_email'].drop()
    post_meta.tables['user'].columns['cyclist_name'].drop()
