from allinone import db

class Servers(db.Model):
    __tablename__ = 'servers'
    id = db.Column(db.Integer, primary_key=True)
    hostname = db.Column(db.String, null=True)
    ip_addr = db.Column(db.String)
    group_id = db.Column(db.ForeignKey("servergroup.id"), ondelete='SET NULL')

class ServerGroup(db.Model):  
    __tablename__ = 'servergroup'
    id = db.Column(db.Integer, primary_key=True)
    groupname = db.Column(db.String(60))