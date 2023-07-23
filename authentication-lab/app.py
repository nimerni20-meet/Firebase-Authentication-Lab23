from flask import Flask, render_template, request, redirect, url_for, flash
from flask import session as login_session
import pyrebase

config = {
  "apiKey": "AIzaSyAvEeJXjtPejmnIphkox18ts4kDAIvQpQ4",
 "authDomain": "lab-c4556.firebaseapp.com",
  "projectId": "lab-c4556",
  "storageBucket": "lab-c4556.appspot.com",
  "messagingSenderId": "980248028540",
  "appId": "1:980248028540:web:197a93e8e7e72f00f670f9",
  "measurementId": "G-KR93543B28",
  "databaseURL":""
}
firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['SECRET_KEY'] = 'super-secret-key'

@app.route('/', methods=['GET', 'POST'])
def signup():
    error = ""
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        try:
            login_session['user'] = auth.create_user_with_email_and_password(email, password)
            return redirect(url_for('signin'))
        except:
            error = "Authentication failed"
    return render_template("signup.html",error=error)

@app.route('/signin', methods=['GET', 'POST'])
def signin():
    error = ""
    if request.method == 'POST':
       email = request.form['email']
       password = request.form['password']
       try:
            login_session['user'] = auth.sign_in_with_email_and_password(email, password)
            return redirect(url_for('add_tweet'))
       except:
            error = "Authentication failed"
    return render_template("signin.html",error=error)

@app.route('/add_tweet', methods=['GET', 'POST'])
def add_tweet():
    return render_template("add_tweet.html")

@app.route('/signout')
def signout():
    login_session['user'] = None
    auth.current_user = None
    return redirect(url_for('signin'))

if __name__ == '__main__':
    app.run(debug=True)








