from allinone import db

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(60))
    user_pw = db.Column(db.String(400))
    dep_id = db.Column(db.Integer,db.ForeignKey("department.id"))
    security_grade = db.Column(db.Integer) # 사용자별 보안 등급

class Department(db.Model):
    __tablename__ = 'department'
    id = db.Column(db.Integer, primary_key=True)
    department_name = db.Column(db.String)
