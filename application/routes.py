from application import app, db
from application.models import Users,Posts
@app.route('/add/<User>')
@app.route('/add/<User>/<first>/<last>')
def add(User,first="null",last="null"):
    new_User = Users(firstName=first,lastName=last,userName=User)
    db.session.add(new_User)
    db.session.commit()
    return f"Added {User} to database"

@app.route('/read')
def read():
    all_Users = Users.query.all()
    Users_string = ""
    for User in all_Users:
        Users_string += "<br>"+  "ID:"+str(User.id) + "||First Name:" + User.firstName + "||Last Name:" + User.lastName + "||User Name:" + User.userName 
    return Users_string

@app.route('/update/<int:id>/<User>/<first>/<last>')
def update(id,User,first,last):
    first_User = Users.query.get(id)
    first_User.firstName = first
    first_User.lastName = last
    first_User.userName = User
    db.session.commit()
    return f"Updated User id {id}"


@app.route('/delete/<int:id>')
def delete(id):
    User = Users.query.get(id)
    db.session.delete(User)
    db.session.commit()
    return f"Deleted User id {id}"



@app.route('/count')
def count():
    all_Users = Users.query.all()
    count=0
    for User in all_Users:
        count+=1
    return f'The number of users in db is {count}'

@app.route('/updatename/<oldUser>/<newUser>')
def updatename(oldUser,newUser):
    first_User = Users.query.filter_by(userName=oldUser).first()
    first_User.userName = newUser
    db.session.commit()
    return f"Updated User {oldUser} to {newUser}"

@app.route('/deletename/<Username>')
def deletename(Username):
    User = Users.query.filter_by(userName=Username).first()
    db.session.delete(User)
    db.session.commit()
    return f"Deleted User {Username}"

