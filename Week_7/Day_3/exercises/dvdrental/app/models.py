# from app import db
# from datetime import datetime
#
#
# class Book(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String(64), nullable=False) #64 is char limit
#     author = db.Column(db.String(50), default='Unknown')
#     pub_date = db.Column(db.DateTime, default=datetime.now, nullable=True)
#     price = db.Column(db.Float, default=5.0)
