from allinone import db
 
class UIViewPermission(db.Model):
    __tablename__ = 'uiviewpermission'
    id = db.Column(db.Integer, primary_key=True)
    access_ui_id = db.Column(db.Integer, db.ForeignKey("uiview.id"))
    allow_user_id = db.Column(db.Integer, db.ForeignKey("user.id"))

class UIView(db.Model):
    __tablename__ = 'uiview'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60))