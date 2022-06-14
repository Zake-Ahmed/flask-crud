from application import app, db
from application.models import Users,Posts
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

@app.route('/update/<int:id>/<user>/<first>/<last>')
def update(id,user,first,last):
    first_user = Users.query.get(id)
    first_user.firstName = first
    first_user.lastName = last
    first_user.userName = user
    db.session.commit()
    return f"Updated user id {id}"


@app.route('/delete/<int:id>')
def delete(id):
    user = Users.query.get(id)
    db.session.delete(user)
    db.session.commit()
    return f"Deleted user id {id}"

