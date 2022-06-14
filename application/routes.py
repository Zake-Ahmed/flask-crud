from application import app, db
from application.models import Users,Posts
@app.route('/add/<User>')
@app.route('/add/<User>/<first>/<last>')
def add(User,first="null",last="null"):
    new_User = UserUsers(firstName=first,lastName=last,UserName=User)
    db.session.add(new_User)
    db.session.commit()
    return f"Added {User} to database"

@app.route('/read')
def read():
    all_UserUsers = UserUsers.querUsery.all()
    UserUsers_string = ""
    for User in all_UserUsers:
        UserUsers_string += "<br>"+  "ID:"+str(User.id) + "||First Name:" + User.firstName + "||Last Name:" + User.lastName + "||UserUser Name:" + User.UserName 
    return UserUsers_string

@app.route('/update/<int:id>/<User>/<first>/<last>')
def update(id,User,first,last):
    first_User = UserUsers.querUsery.get(id)
    first_User.firstName = first
    first_User.lastName = last
    first_User.UserName = User
    db.session.commit()
    return f"Updated User id {id}"


@app.route('/delete/<int:id>')
def delete(id):
    User = UserUsers.querUsery.get(id)
    db.session.delete(User)
    db.session.commit()
    return f"Deleted User id {id}"

