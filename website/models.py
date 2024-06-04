from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func


class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    notes = db.relationship('Note')


# class emailAuth(db.Model):
#     auth_id = db.Column(db.Integer)
#     userEmail = db.Column(db.Varchar)
#     authStr = db.Column(db.Varchar)

# class imageBoard(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     workspaceTitle = db.Column(db.Varchar)
#     ext = db.Column(db.Varchar)
#     type = db.Column(db.Varchar)
#     bitRate = db.Column(db.Varchar)
#     size = db.Column(db.Varchar)
#     codecName = db.Column(db.Varchar)
#     width = db.Column(db.Integer)
#     height = db.Column(db.Integer)
#     pixFmt = db.Column(db.Varchar)
#     duration = db.Column(db.Float)
#     fps = db.Column(db.Integer)
#     user_id = db.Column(db.Varchar)
#     status = db.Column(db.Varchar)
#     filename = db.Column(db.Varchar)
#     originalname = db.Column(db.Varchar)
#     outputUrl = db.Column(db.Varchar)
#     koreaCreate = db.Column(db.Varchar)
#     timestamp = db.Column(db.Integer)
#     workspace = db.Column(db.Integer)
#     srImage = db.Column(db.Integer)

# class srBoard(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     filename = db.Column(db.Varchar)
#     originalname = db.Column(db.Varchar)
#     srtype = db.Column(db.Varchar)
#     srUrl = db.Column(db.Varchar)
#     user_id = db.Column(db.Varchar)
#     workspaceTitle = db.Column(db.Varchar)
#     scale = db.Column(db.Integer)
#     format = db.Column(db.Varchar)
#     jobid = db.Column(db.Varchar)
#     enhancedname = db.Column(db.Varchar)
#     srStatus = db.Column(db.Varchar)
#     type = db.Column(db.Varchar)
#     progress = db.Column(db.Integer)
#     originalboard = db.Column(db.Integer)
#     create = db.Column(db.Varchar)
#     workspace = db.Column(db.Integer)

# class sr_task(db.Model):
#     task_id = db.Column(db.Integer, primary_key=True)
#     user_id = db.Column(db.Varchar)
#     request_num = db.Column(db.Integer)
#     request_date = db.Column(db.Integer)
#     complete_date = db.Column(db.Integer)
#     sr_type = db.Column(db.Varchar)
#     scale = db.Column(db.Varchar)
#     filename = db.Column(db.Varchar)
#     storage_origin = db.Column(db.Varchar)
#     storage_sr = db.Column(db.Varchar)
#     sr_status = db.Column(db.Varchar)
#     sr_progress = db.Column(db.Integer)
#     media_width = db.Column(db.Integer)
#     media_height = db.Column(db.Integer)
#     media_total_frame = db.Column(db.Integer)
#     api_key = db.Column(db.Varchar)

# class workspace(db.Model):
#     id = db.Column(db.Integer)
#     workspace = db.Column(db.Varchar)
#     user_id = db.Column(db.Varchar)
#     timestamp = db.Column(db.timestamp)
#     korea_create = db.Column(db.Varchar)
#     imageBoard = db.Column(db.Varchar) 
#     SrImage = db.Column(db.Varchar)


    