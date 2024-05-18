from allinone import db

class ServerService:
    __tablename__ = 'serverservice'
    id = db.Column(db.Integer, primary_key=True)
    server_id = db.Column(db.Integer, db.ForeignKey("servers.id"))
    service_name = db.Column(db.String(30)) # SSH
    port = db.Column(db.Integer)
    protocol = db.Column(db.String(10))
    ctype = db.Column(db.Integer, db.ForeignKey('credentialstype.id'))
    user_id = db.Column(db.String(60))
    user_pw = db.Column(db.String(60))
    pem_base64 = db.Column(db.Text)
    
class CredentialType(db.Model):
    __tablename__ = 'credentialstype'
    id = db.Column(db.Integer, primary_key=True)
    type_name = db.Column(db.String(30))
