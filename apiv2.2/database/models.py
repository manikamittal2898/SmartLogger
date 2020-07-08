from .db import db

class Log(db.DynamicDocument):
    timestamp8601 = db.StringField(required=False)
    message = db.StringField( required=False)
    cf_app_name = db.StringField( required=False)  
    level = db.StringField( required=False)  
    Error_Message = db.StringField()
    Exception_Details = db.StringField()
    Exception_Name = db.StringField(required=False) 

class Comments(db.DynamicDocument):
    pass