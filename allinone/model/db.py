import db


class DBHistory(db.Model):
    __tablename__ = 'history'
    id = db.Column(db.Integer, primary_key=True)
    ServerName = db.Column(db.String)
    Message = db.Column(db.String)
    

    def __repr__(self):
        return '<DBHistory %r>' % self.id