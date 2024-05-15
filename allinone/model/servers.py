from allinone import db

class Servers(db.Model):
    __tablename__ = 'servers'
    id = db.Column(db.Integer, primary_key=True)
    hostname = db.Column(db.String, null=True)
    ip_addr = db.Column(db.String)