from application import app, db
from application.models import Users
@app.route('/add/<user>')
@app.route('/add/<user>/<first>/<last>')
def add(user,first="null",last="null"):
    new_user = Users(firstName=first,lastName=last,userName=user)
    db.session.add(new_user)
    db.session.commit()
    return f"Added {user} to database"

@app.route('/read')
def read():
    all_Users = Users.query.all()
    Users_string = ""
    for user in all_Users:
        Users_string += "<br>"+  "ID:"+str(user.id) + "||First Name:" + user.firstName + "||Last Name:" + user.lastName + "||User Name:" + user.userName 
    return Users_string

@app.route('/update/<name>/<int:id>')
def update(name,id):
    first_user = Users.query.get(id)
    first_user.name = name
    db.session.commit()
    return first_user.name
