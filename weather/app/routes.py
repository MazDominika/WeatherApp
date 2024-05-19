from app import app
from app.forms import LoginForm
from app.models import User, Measurments
from flask import render_template, redirect, send_file, jsonify
from flask_login import current_user, login_user, logout_user
from app import db
from flask import flash
import sqlalchemy as sa


@app.route('/', methods = ['POST', 'GET'])
@app.route('/login', methods = ['POST', 'GET'])
def login():
    if current_user.is_authenticated:
        return redirect('/sensormeasurments')
    
    form = LoginForm()
    if form.validate_on_submit():
        user = db.session.scalar(
            sa.select(User).where(User.username == form.username.data))
        
        if user is None or not user.check_password(form.password.data):
            return redirect('/login')
    
        login_user(user, remember=form.remember_me.data)
        return redirect('/sensormeasurments')
    
    return render_template('loginpage.html', form = form, current_user = current_user)

@app.route('/logout')
def logout():
    logout_user()
    return redirect('/login')

@app.route('/sensormeasurments')
def sensormeasurments():
    if current_user.is_authenticated:
        return render_template('sensormeasurmentspage.html')
    return redirect('/login')


@app.route('/manualcontrol')
def manualcontrol():
    if current_user.is_authenticated:
        return render_template('manualcontrolpage.html')
    return redirect('/login')


@app.route('/get_json', methods=['GET'])
def get_json():
    if current_user.is_authenticated:
        measurement = db.session.execute(sa.select(Measurments.date, Measurments.temperature, Measurments.pressure, Measurments.humidity).order_by(Measurments.date.desc()).limit(50)).fetchall()
        measurement_json = {
                "date" : [d.strftime("%H:%M:%S") for d,_,_,_ in measurement],
                "temperature": [t for _,t,_,_ in measurement],
                "pressure" : [p for _,_,p,_ in measurement],
                "humidity" : [h for _,_,_,h in measurement]
            }

    return jsonify(measurement_json)

