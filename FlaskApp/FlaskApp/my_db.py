from flask_sqlalchemy import SQLAlchemy

# Initialize the SQLAlchemy object
db = SQLAlchemy()

class UserTable(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(4096))
    user_id = db.Column(db.Integer)
    token = db.Column(db.String(4096))
    login = db.Column(db.Integer)
    access_level = db.Column(db.Integer)
    

    def __init__(self, name, user_id, token, login, access_level):
        self.name = name
        self.user_id = user_id
        self.token = token
        self.login = login
        self.access_level = access_level

# Database utility functions
def delete_all():
    try:
        db.session.query(UserTable).delete()
        db.session.commit()
    except Exception as e:
        print("Delete failed " + str(e))
        db.session.rollback()

def get_user_row_if_exists(user_id):
    return UserTable.query.filter_by(user_id=user_id).first()

def add_user_and_login(name, user_id):
    row = get_user_row_if_exists(user_id)
    if row:
        row.login = 1
        db.session.commit()
    else:
        new_user = UserTable(name, user_id, None, 1, 0)
        db.session.add(new_user)
        db.session.commit()

def user_logout(user_id):
    row = get_user_row_if_exists(user_id)
    if row:
        row.login = 0
        db.session.commit()

def add_token(user_id, token):
    row = get_user_row_if_exists(user_id)
    if row:
        row.token = token
        db.session.commit()

def get_token(user_id):
    row = get_user_row_if_exists(user_id)
    if row:
        return row.token

def view_all():
    users = UserTable.query.all()
    for user in users:
        print(f"{user.id} | {user.name} | {user.user_id} | {user.token} | {user.access_level}")

def get_all_logged_in_users():
    logged_in_users = UserTable.query.filter_by(login=1).all()
    return [{"name": user.name, "user_id": user.user_id, "access_level": user.access_level} for user in logged_in_users]

def add_user_permission(user_id, read, write):
    row = get_user_row_if_exists(user_id)
    if row:
        if read and write:
            row.access_level = 2
        elif read:
            row.access_level = 1
        else:
            row.access_level = 0
        db.session.commit()

def get_user_access(user_id):
    row = get_user_row_if_exists(user_id)
    if row:
        return {
            "read": row.access_level >= 1,
            "write": row.access_level == 2
        }
