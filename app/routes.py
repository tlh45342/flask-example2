from flask import render_template, request, flash, session, url_for, redirect
from flask_login import logout_user, login_required, current_user
from flask_login import LoginManager, UserMixin, login_required, login_user, logout_user, current_user
from app import app

# -----------------------------

@app.route('/', methods=['GET'])
def default():
  return render_template("welcome.html")

@login_manager.user_loader
def load_user(user_id):
   conn = sqlite3.connect('login.db')
   curs = conn.cursor()
   curs.execute("SELECT * from login where user_id = (?)",[user_id])
   lu = curs.fetchone()
   if lu is None:
      return None
   else:
      return User(int(lu[0]), lu[1], lu[2])
      
@app.route("/login", methods=['GET','POST'])
def login():
  if current_user.is_authenticated:
     return redirect(url_for('profile'))
  form = LoginForm()
  if form.validate_on_submit():
     conn = sqlite3.connect('login.db')
     curs = conn.cursor()
     curs.execute("SELECT * FROM login where email = (?)", [form.email.data])
     user = list(curs.fetchone())
     Us = load_user(user[0])
     if form.email.data == Us.email and form.password.data == Us.password:
        login_user(Us, remember=form.remember.data)
        Umail = list({form.email.data})[0].split('@')[0]
        redirect(url_for('profile'))
  return render_template('login.html',title='Login', form=form)

@app.route("/profile",)
def profile():
  return render_template("welcome.html")
  
@app.route('/logout')
@login_required
def logout():
    logout_user()
    if session.get('was_once_logged_in'):
        # prevent flashing automatically logged out message
        del session['was_once_logged_in']
    flash('You have successfully logged yourself out.')
    return redirect('/login')
