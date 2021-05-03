from flask import Flask, render_template, request, send_file, flash, redirect, url_for
from models import user, db
from form import registration

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

@app.route("/signup", methods=["POST", "GET"])
def signup():
  form = registration()
  if form.validate_on_submit():
    member = user(
      first_name = form.first_name.data,
      second_name = form.second_name.data,
      last_name = form.last_name.data,
      email = form.email_address.data,
      phone_number = form.phone_number.data,
      username = form.username.data,
      password = form.password.data,
      )
    db.session.add(member)
    db.session.commit()
    return redirect(url_for('login'))

  if form.errors != {}:
    for err_msg in form.errors.values():
      flash(f'There was an error creating the user: {err_msg}', category='danger')

  return render_template("signup.html", form=form)

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

@app.route('/logout')
def logout():
  return render_template("signin.html", success="Logged out successfully")

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
