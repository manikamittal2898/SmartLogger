from .db import db

class Log(db.Document):
    timestamp8601 = db.StringField(required=True)
    message = db.StringField( required=True)
    cf_app_name = db.StringField( required=True)  
    level = db.StringField( required=True)  
    Error_Message = db.StringField()
    Exception_Details = db.StringField()
    Exception_Name = db.StringField(required=True) 