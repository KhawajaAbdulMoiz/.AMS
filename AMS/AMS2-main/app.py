from flask import Flask,render_template,request,url_for,redirect,flash,session
from werkzeug.security import generate_password_hash, check_password_hash
import os

app = Flask(__name__)

# Set secret key
app.secret_key = os.urandom(24)

users={}

announcements = []

# Define a list to store contact form submissions
contact_submissions = []

# Limit the number of contact form submissions to 10
MAX_SUBMISSIONS = 10

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/admin')
def admin():
    return render_template('admin.html')

@app.route('/signup')
def signup():
    return render_template('signupform.html')

@app.route('/signup',methods=["POST"])
def signup_post():
    if request.method=='POST':
        First_Name = request.form.get('first_name')
        Last_Name = request.form.get('last_name')
        Email_id= request.form.get ('email')
        Contact = request.form.get ('contact')
        Password = request.form.get ('password')
        Confirm_Password=request.form.get('confirm_password')
        if all([First_Name, Last_Name, Email_id, Contact, Password, Confirm_Password]):
            # Form submission is successful, redirect to login page
            if Password == Confirm_Password:
                # Hash the password
                hashed_password = generate_password_hash(Password)
                # Add email and hashed password to the users dictionary
                users[Email_id] = hashed_password
                # Redirect to login page after successful signup
                return redirect(url_for('login_page'))
            else:
                # Passwords do not match, redirect to signup page with error message
                flash('Passwords do not match. Please try again.', 'error')
                return redirect(url_for('signup'))
        else:
            # Form submission failed, render the signup form again
            return redirect(url_for('signup'))
    return render_template('signupform.html')


@app.route('/login')
def login_page():
    return render_template('login.html')

@app.route('/login_page',methods=["POST","Get"])
def login_post():
    if request.method=='POST':
        Email = request.form.get('email').lower()
        Password = request.form.get('password')
        if Email == 'mabdullahuit19b@gmail.com'.lower() and Password == '0987':
        # Redirect to admin page if admin credentials are provided
            return redirect(url_for('admin'))
        elif Email in users and check_password_hash(users[Email], Password):
            # Retrieve first_name and last_name from the form
            first_name = request.form.get('first_name')
            last_name = request.form.get('last_name')
            # Store first_name and last_name in session
            session['first_name'] = first_name
            session['last_name'] = last_name
            return redirect(url_for('owner'))
        else:
            # Username or Password is incorrect, try again
            flash('Invalid email or password', 'error')
            return redirect(url_for('login_page'))
    return render_template('login.html')

    
@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/handle_contact_form', methods=['POST'])
def handle_contact_form():
    if request.method == 'POST':
        # Extract form data
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        message = request.form['message']
        # Store the form data in the contact_submissions list
        contact_submissions.append({
            'first_name': first_name,
            'last_name': last_name,
            'email': email,
            'message': message,
        })
        # Limit the number of submissions to 10
        if len(contact_submissions) > MAX_SUBMISSIONS:
            contact_submissions.pop(0)  # Remove the oldest submission
        # Redirect the user back to the home page
        return redirect(url_for('home'))    

@app.route('/requests')
def requests_page():
    # Get the last 10 submitted contact form data
    last_submissions = contact_submissions[-10:] if contact_submissions else []
    return render_template('requests.html', last_submissions=last_submissions)


@app.route('/Members')
def Members():
    return render_template('Members.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/owner',methods=["GET","POST"])
def owner():
    first_name = session.get('first_name')  # Get first_name from session
    last_name = session.get('last_name')  # Get last_name from session
    return render_template('owner.html', first_name=first_name,last_name=last_name) # Pass first_name to owner

@app.route('/Announcement')
def Announcement():
    return render_template('Announcement.html')

@app.route('/submit_announcement', methods=['POST'])
def submit_announcement():
    announcement_text = request.json.get('text')
    # Process the announcement (store it in a database, etc.)
    # Here, for demonstration, let's add it to a list
    announcements.append(announcement_text)
    return 'OK', 200

@app.route('/maintainance')
def maintainance():
    return render_template('maintainance.html')

@app.route('/Make_Announcement')
def Make_announcement():
    return render_template('Make_announcement.html')

if __name__ == '__main__':
    app.run(debug=True)
