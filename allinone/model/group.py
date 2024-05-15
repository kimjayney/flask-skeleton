from allinone import db

class CredentialsGroup(db.Model):  
    __tablename__ = 'credentialsgroup'
    id = db.Column(db.Integer, primary_key=True)
    groupname = db.Column(db.String(60))

# Usecase: AssignedGroupService 를 통해, group id만 알면 서비스 정보를 알 수 있다.
class AssignedGroupService(db.Model):
    __tablename__ = 'assignedgroupservice'
    id = db.Column(db.Integer, primary_key=True)
    group_id = db.Column(db.Integer, db.ForeignKey("credentialsgroup.id"))
    service_id = db.Column(db.Integer, db.ForeignKey('serverservice.id'))

#Usecase: Group id 만 있으면 CredentialId 를 뽑을 수 있다.
#이 테이블이 없어도 AssignedGroupService의 service_id 를 통해 Credentials 테이블로 유저 정보들을 갖고올 수 있다. (딱봐도 조인쓰고 귀찮아 질 것이 뻔하다)
#그룹 아이디로 그냥 인증 정보를 바로 받아올 수 있게 하기 위한 테이블이다.

class AssignedGroupServerCredential(db.Model):
    __tablename__ = 'assignedgroupcredentiallist'
    id = db.Column(db.Integer, primary_key=True)
    group_id = db.Column(db.Integer, db.ForeignKey("credentialsgroup.id"), ondelete='CASCADE')
    credential_id = db.Column(db.Integer, db.ForeignKey("credentials.id")) 

# 그룹 아이디로 그냥 서버 정보만 갖고오기 위한 테이블이다.
class AssignedGroupServerList(db.Model):
    __tablename__ = 'assignedgroupserverlist'
    id = db.Column(db.Integer, primary_key=True)
    group_id = db.Column(db.Integer, db.ForeignKey("credentialsgroup.id"), ondelete='CASCADE')
    server_id = db.Column(db.Integer, db.ForeignKey("servers.id"), ondelete='CASCADE') 

# 이거로 내가(user가) 어느 그룹들에 속해있는지 리스트를 뽑아준다.
class AssignedGroupServerUser(db.Model): # 여러 유저가 여러개 그룹에 할당할수도 있어야 한다.
    __tablename__ = 'assignedgroup'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), null=True, ondelete="all,delete")
    dep_id = db.Column(db.Integer, db.ForeignKey("department.id"), null=True)
    group_id = db.Column(db.Integer, db.ForeignKey("credentialsgroup.id"), ondelete='CASCADE')