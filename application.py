import os

from flask import Flask, render_template, request, send_file
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

app = Flask(__name__)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

engine = create_engine('mssql://KEVINKAGWIMA/alphataji?driver=sql server?trusted_connection=yes')
db = scoped_session(sessionmaker(bind=engine))

@app.route("/")
@app.route("/home")
def index():
  return render_template("index.html")

@app.route("/contact")
def contact():
  return render_template("contact.html")

@app.route("/about us")
def about():
  return render_template("about us.html")

@app.route("/services")
def services():
  return render_template("services.html")

@app.route("/faq")
def faq():
  return render_template("faq.html")

@app.route("/Management Team")
def team():
  return render_template("team.html")

@app.route("/merchendise")
def merchendise():
  return render_template("merchendise.html")

@app.route("/signup")
def signup():
  return render_template("signup.html")

@app.route("/register", methods=["POST"])
def register():
  fname = request.form.get("fname")
  sname = request.form.get("sname")
  lname = request.form.get("lname")
  email = request.form.get("email")
  phone = request.form.get("phone")
  username = request.form.get("username")
  password = request.form.get("password")

  if db.execute("SELECT username, email, phone_number FROM members WHERE username=:username or email=:email or phone_number=:phone", {"username":username, "email":email, "phone":phone}).rowcount != 0:
    return render_template("signup.html", message="Email, phone number or username already exists. Try again")
  
  db.execute("INSERT INTO members (first_name, second_name, last_name, email, phone_number, username, password) VALUES (:first_name, :second_name, :last_name, :email, :phone_number, :username, :password)", {"first_name":fname, "second_name":sname, "last_name":lname, "email":email, "phone_number":phone, "username":username, "password":password})

  db.commit()
  return render_template("signin.html", success="User registred.")

@app.route("/signin")
def login():
  return render_template("signin.html")

@app.route("/authenticate", methods=["POST"])
def authenticate():
  username = request.form.get("username")
  password = request.form.get("password")

  if db.execute("SELECT username, password FROM members WHERE username=:username and password=:password", {"username":username, "password":password}).rowcount == 0:
    return render_template("signin.html", message="Invalid Credentials")

  return render_template("index.html", name=username, message="logged in as")

@app.route('/download')
def download_file():
  path = "branch-loan-form.pdf"
  return send_file(path, as_attachment=True)

@app.route('/download2')
def download_file_2():
  path = "golden-loan-form.pdf"
  return send_file(path, as_attachment=True)

@app.route('/download3')
def download_file_3():
  path = "express-loan-form.pdf"
  return send_file(path, as_attachment=True)

@app.route('/download4')
def download_file_4():
  path = "normal-loan-form.pdf"
  return send_file(path, as_attachment=True)

@app.route('/download5')
def download_file_5():
  path = "supersaver-loan-form.pdf"
  return send_file(path, as_attachment=True)

@app.route('/download6')
def download_file_6():
  path = "super-loan-form.pdf"
  return send_file(path, as_attachment=True)

@app.route('/download7')
def download_file_7():
  path = "msingi-loan-form.pdf"
  return send_file(path, as_attachment=True)

@app.route('/download8')
def download_file_8():
  path = "dividends advance-loan-form.pdf"
  return send_file(path, as_attachment=True)

@app.route('/download9')
def download_file_9():
  path = "benovelent fund-form.pdf"
  return send_file(path, as_attachment=True)
