from db.db_migration import db
 
class User(db.Model):
    __tablename__ = 'tb_user'
 
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String())
    age = db.Column(db.Integer())
    phone = db.Column(db.String(), unique=True)
 
    def __init__(self, *args, **kwargs):
        super(User, self).__init__(**kwargs)
 
    def __repr__(self):
        return f"{self.name}:{self.age}"