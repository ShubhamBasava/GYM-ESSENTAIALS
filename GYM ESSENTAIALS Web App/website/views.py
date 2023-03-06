
from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required,current_user
from .models import Feedback
from . import db
from datetime import date,timedelta

# Creating "views" Blueprint
views = Blueprint('views', __name__)

# HTML page view (home page route)
@views.route('/',methods=['GET','POST'])
def home():
    return render_template("index.html", user=current_user)


# HTML page view (Book Car route)
# @views.route('/book-car',methods=['GET','POST'])
# @login_required
# def bookcar():

#     #cars = Car.query.order_by(Car.model).all()
#     if request.method == 'POST':

#         if 'find_car_submit' in request.form:

#             car_model = request.form.get('car_model')

#             if car_model == 'GR-Supra':
#                 car = Car.query.filter_by(model="GR").first()
#                 # print(car.car_name)
#                 return render_template("book-car.html", user=current_user, car=car)
#             elif car_model == 'GR-86':
#                 car = Car.query.filter_by(model="GR 86").first()
#                 return render_template("book-car.html", user=current_user, car=car)
#             elif car_model == 'GT-IV':
#                 car = Car.query.filter_by(model="GT4").first()
#                 return render_template("book-car.html", user=current_user, car=car)
#             elif car_model == '2000-GT':
#                 car = Car.query.filter_by(model="2000 GT").first()
#                 return render_template("book-car.html", user=current_user, car=car)
#             elif car_model == 'MK-IV':
#                 car = Car.query.filter_by(model="MK IV").first()
#                 return render_template("book-car.html", user=current_user, car=car)
#             else : 
#                 flash('Unable to fetch the car details right now!!!', category='error')
#                 return render_template("book-car.html", user=current_user)

#         if 'book_car_submit' in request.form:
            
#             name = request.form.get('name')
#             email = request.form.get('email')
#             mobile = request.form.get('mobile')
#             city = str(request.form.get('city'))
#             country = request.form.get('country')
#             address = request.form.get('address')
#             model_name = request.form.get('car_model')

#             car_info = Car.query.filter_by(model=model_name).first()

#             if len(name) < 5 :
#                 flash('Name is too short', category='error')
#             elif len(city) < 3 : 
#                 flash('Invalid city name', category='error')
#             elif len(country) < 3 :
#                 flash('Invalid country name', category='error')
#             else : 
#                 uid = current_user.id
#                 b_date = date.today()
#                 # d_date = b_date + timedelta(days=random(7,15))
#                 d_date = b_date + timedelta(days=20)
#                 car_model = car_info.model
#                 car_name = car_info.car_name

#                 book_car = Booking(user_id=uid,contact_email=email,booking_name=name,contact_mobile=mobile,contact_address=address,city=city,country=country, car_model=car_model,car_name=car_name,booking_date=b_date,delivary_date=d_date)

#                 db.session.add(book_car)
#                 db.session.commit()
                
                

#                 flash('Your Dream Car Has Been Booked Succesfully!.', category="success")
#                 return redirect(url_for('views.profile'))

#     return render_template("book-car.html", user=current_user)

# HTML page view (Concept Car route)
# @views.route('/concept-cars')
# def conceptcar():
#     return render_template("concept-cars.html", user=current_user)


# HTML page view (Dashboard)
# @views.route('/profile')
# #@login_required
# def profile():
#     car_details = Car.query.all()

#     return render_template("profile.html", user = current_user, car_details=car_details)


# HTML page view (contact page route)
@views.route('/contact', methods=['GET','POST'])
def contact():
    if request.method == 'POST':
        email = request.form.get('email')
        name = request.form.get('name')
        subject = request.form.get('subject')
        message = request.form.get('message')

        if len(name) < 2 :
            flash('Please provide a valid name.', category="error")
        elif len (email) < 6 :
            flash('Please provide a valid email.', category="error")
        elif len(subject) < 2:
            flash('Please specify subject properly.', category="error")
        elif len(message) < 10 : 
            flash('Message is too short!', category="error")
        else : 
            query = Feedback(email=email,name=name,subject=subject,message=message)
            db.session.add(query)
            db.session.commit()
            
            flash('Email sent succefully. We\'ll get back too you soon!..', category="success")
    return render_template("contact.html", user = current_user )


# HTML page view (about page)
@views.route('/about')
def about():
    return render_template("about.html", user = current_user)

'''
# HTML page view (ADD STAION RECORD Temp)
@views.route('/add-car', methods=['GET','POST'])
def tempform():
    if request.method == 'POST':
        model_no = request.form.get('model_no')
        name = request.form.get('name')
        year = request.form.get('year')
        price = request.form.get('price')
        desc = request.form.get('desc')

        new_row = Car(model=model_no,car_name=name,release_year=year,price=price,description=desc)
        
        db.session.add(new_row)
        db.session.commit()
            
        flash('DATA ADDED Succesfully!.', category="success")

    else : 
        flash('Unable to add data', category='error')


    return render_template("tempform.html")
'''