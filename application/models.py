from application import db


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    userName = db.Column(db.String(30))
    firstName = db.Column(db.String(30),nullable = True)
    lastName = db.Column(db.String(30),nullable = True)
    #post=db.relationship('Post', backref='users')



class Posts(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    message= db.Column(db.String(280),nullable = False)
    likes = db.Column(db.Integer,nullable = True)
    userID = db.Column(db.Integer , db.ForeignKey(Users.id), nullable=False)
 