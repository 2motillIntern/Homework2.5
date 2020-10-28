from Avenger_Phone_App import app 

from flask import render_template,request

from Avenger_Phone_App.forms import UserInfoForm

@app.route('/')
def home():
    return render_template('home.html')


@app.route('register', methods = ['GET', 'POST'])
def register():
    form = UserInfoForm
    if request.method == 'POST' and form.validate():
        name = form.name.data 
        email = form.email.data
        phone = form.phone.data
        password = form.email.data 
        print(name,email, phone, password)
    return render_template('register.html', user_form = form)