from flask import render_template

from application import app


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', title='Homepage')


@app.route('/about')
def about():
    return render_template('about.html', title='About')


@app.route('/booking')
def booking():
    return render_template('booking.html', title='Booking')


@app.route('/courses')
def courses():
    return render_template('courses.html', title='Courses')


@app.route('/confirmation')
def confirmation_message():
    return render_template('confirmation.html', title='Confirmation Message')


@app.route('/contact')
def contact():
    return render_template('contact.html', title='Contact Us')


@app.route('/instructors')
def instructors():
    return render_template('instructors.html', title='Instructors')


@app.route('/faq')
def faq():
    return render_template('faq.html', title='FAQs')


@app.route('/admin')
def admin():
    return render_template('admin.html', title='Confirmed Bookings')


