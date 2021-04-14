import os
from flask import Flask, render_template, request, send_file
from models import *

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = ('mssql://KEVINKAGWIMA/alphataji?driver=sql server?trusted_connection=yes')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

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
  firstname = request.form.get("fname")
  secondname = request.form.get("sname")
  lastname = request.form.get("lname")
  email = request.form.get("email")
  phone = request.form.get("phone")
  username = request.form.get("username")
  password = request.form.get("password")
  
  member = (
    user(first_name=firstname,second_name=secondname,last_name=lastname,email=email,phone_number=phone,username=username,password=password
    )
  )

  email_exists = db.session.query(user).filter_by(email=email).first()
  if email_exists is not None:
    return render_template("signup.html", message="Email already exists. Try again")

  phonenumber_exists = db.session.query(user).filter_by(phone_number=phone).first()
  if phonenumber_exists is not None:
    return render_template("signup.html", message="Phone number already exists. Try again")
  
  username_exists = db.session.query(user).filter_by(username=username).first()
  if username_exists is not None:
    return render_template("signup.html", message="Username already exists. Try again")

  db.session.add(member)
  
  db.session.commit()
  return render_template("signin.html", success="User registred.")

@app.route("/signin")
def login():
  return render_template("signin.html")

@app.route("/authenticate", methods=["POST"])
def authenticate():
  username = request.form.get("username")
  password = request.form.get("password")

  check_username = db.session.query(user.username).filter_by(username=username).first()
  if check_username is None:
    return render_template("signin.html", message="Invalid username")

  check_password = db.session.query(user.username).filter_by(password=password).first()
  if check_password is None:
    return render_template("signin.html", message="Invalid password")

  return render_template("index.html", name=username, message="logged in as")

@app.route('/download')
def download_file():
  path = "Loan Forms/branch-loan-form.pdf"
  return send_file(path, as_attachment=True)

@app.route('/download2')
def download_file_2():
  path = "Loan Forms/golden-loan-form.pdf"
  return send_file(path, as_attachment=True)

@app.route('/download3')
def download_file_3():
  path = "Loan Forms/express-loan-form.pdf"
  return send_file(path, as_attachment=True)

@app.route('/download4')
def download_file_4():
  path = "Loan Forms/normal-loan-form.pdf"
  return send_file(path, as_attachment=True)

@app.route('/download5')
def download_file_5():
  path = "Loan Forms/supersaver-loan-form.pdf"
  return send_file(path, as_attachment=True)

@app.route('/download6')
def download_file_6():
  path = "Loan Forms/super-loan-form.pdf"
  return send_file(path, as_attachment=True)

@app.route('/download7')
def download_file_7():
  path = "Loan Forms/msingi-loan-form.pdf"
  return send_file(path, as_attachment=True)

@app.route('/download8')
def download_file_8():
  path = "Loan Forms/dividends advance-loan-form.pdf"
  return send_file(path, as_attachment=True)

@app.route('/download9')
def download_file_9():
  path = "Loan Forms/benovelent fund-form.pdf"
  return send_file(path, as_attachment=True)
