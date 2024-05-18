from allinone import db
 
class UIViewPermission(db.Model):
    __tablename__ = 'uiviewpermission'
    id = db.Column(db.Integer, primary_key=True)
    access_ui_id = db.Column(db.Integer, db.ForeignKey("uiview.id"))
    allow_dep_id = db.Column(db.Integer, db.ForeignKey("department.id"))
    access_security_grade = db.Column(db.Integer) # 보안 등급에 따라 UI View 접근 가능

class UIView(db.Model):
    __tablename__ = 'uiview'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60))
