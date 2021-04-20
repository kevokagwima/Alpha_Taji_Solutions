from flask import Flask, render_template, request, send_file, flash
from models import user, db

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = ('mssql://KEVINKAGWIMA/alphataji?driver=sql server?trusted_connection=yes')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'f4cedd9fad0d4aae6af66788'
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
  password1 = request.form.get("password1")
  
  member = (
    user(first_name=firstname,second_name=secondname,last_name=lastname,email=email,phone_number=phone,username=username,password=password
    )
  )

  email_exists = db.session.query(user).filter_by(email=email).first()
  if email_exists is not None:
    flash("Email already exists. Please try another email")
    return render_template("signup.html")

  phonenumber_exists = db.session.query(user).filter_by(phone_number=phone).first()
  if phonenumber_exists is not None:
    flash("Phone number already exists. Please try another Phone number")
    return render_template("signup.html")
  
  username_exists = db.session.query(user).filter_by(username=username).first()
  if username_exists is not None:
    flash("Username already exists. Please try another username")
    return render_template("signup.html")

  if len(phone) != 10:
    flash("Enter a valid Phone Number")
    return render_template("signup.html")
  
  if len(username) or len(password1) < 5:
    flash("Username or password must be more than 5 characters long")
    return render_template("signup.html")

  if password1 != password:
    flash("Passwords do not match")
    return render_template("signup.html")

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

  check_user = db.session.query(user).filter_by(username=username, password=password).first()
  if check_user is None:
    return render_template("signin.html", message="Invalid credentials")

  return render_template("index.html", name=username)

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
