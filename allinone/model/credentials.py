from allinone import db

class CredentialType(db.Model):
    __tablename__ = 'credentialstype'
    id = db.Column(db.Integer, primary_key=True)
    type_name = db.Column(db.String(30))

class Credentials(db.Model):
    __tablename__ = 'credentials'
    id = db.Column(db.Integer, primary_key=True)
    ctype = db.Column(db.Integer, db.ForeignKey('credentialstype.id'))
    user_id = db.Column(db.String(60))
    user_pw = db.Column(db.String(60))
    pem_base64 = db.Column(db.Text)
    service_id = db.Column(db.Integer, db.ForeignKey('serverservice.id'))
