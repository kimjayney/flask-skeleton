from allinone import db

class ServerService:
    __tablename__ = 'serverservice'
    id = db.Column(db.Integer, primary_key=True)
    server_id = db.Column(db.Integer, db.ForeignKey("servers.id"))
    service_name = db.Column(db.String(30)) # SSH
    port = db.Column(db.Integer)
    protocol = db.Column(db.String(10)) 
    
