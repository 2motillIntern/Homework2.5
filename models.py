from Avenger_Phone_App import app, db 

from werkzeug.security import generate_password_hash, check_password_hash

from datetime import datetime

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(150), nullable = False, unique = True)
    email = db.Column(db.String(100), nullable = False, unique = True)
    phone = db.Column(db.String(15), nullable = False, unique = True)
    password = db.Column(bd.String(20), nullable = False)

    def __init__(self, name, email, phone, password):
        self.name = name
        self.email = email
        self.phone = phone
        self.password = self.set_password(password)

    def set_password(self, password):
        self.pw_hash = generate_password_hash(password)
        return self.pw_hash
    
    def __repr__(self):
        return f'{self.username} is now linked with the following email address: {self.email}'

class Post(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(100))
    content = db.Column(db.String(300))
    date_created = db.Column(db.DateTime, nullable = False, default = datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)

    def __init__(self,title,content,user_id):
    self.title = title
    self.content = content
    self.user_id = user_id

def __repr__(self):
    return f'The title of the post is {self.title} \n and the content is {self.content}'

    
