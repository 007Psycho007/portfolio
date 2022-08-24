from flask import Flask, request, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.sqlite import TEXT, JSON
from db import secrets 
import requests
from json import loads
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db/portfolio.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Projects(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    type = db.Column(db.String(255), unique=False)
    description = db.Column(db.String(255), unique=False)
    long_description = db.Column(TEXT(), unique=False)
    url = db.Column(db.String(255), unique=False, nullable=True)
    used_technologies = db.Column(JSON(), unique=False, nullable=False)
    features = db.Column(JSON(), unique=False, nullable=False)
    def __repr__(self):
        return f'<Project: {self.name}>'
    
class Technologies(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), unique=True, nullable=False)
    level = db.Column(db.Integer)
    
    def __repr__(self):
        return f'<Skill: {self.name}>'
    
class Skills(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), unique=True, nullable=False)
    short_desc = db.Column(db.String(255), unique=False, nullable=False)
    
# Normally I would write a seperate module for Backendfunctions but since this is the only one which I need I put in the controller
def mailsend(subject,text,sender):
    try:
        context = ssl.create_default_context()
        server = smtplib.SMTP('smtp.gmail.com','587')
        server.ehlo() # Can be omitted
        server.starttls(context=context) # Secure the connection
        server.ehlo() # Can be omitted
        server.login(secrets.mail, secrets.mail_pass)

        message = MIMEMultipart("alternative")
        message["Subject"] = subject
        message["From"] = sender
        message["To"] = secrets.recipient
        print(text)
        message.attach(MIMEText(text, "plain"))

        
        
        server.sendmail(sender, secrets.recipient, message.as_string())
        return True
    except Exception as e:
        return False
    finally:
        server.quit() 

@app.route("/", methods=["GET"])
def index():
    
    return render_template("index.html",
                        title="Portfolio of Jan Peterhänsel",
                        technologies=Technologies.query.all(),
                        projects=Projects.query.all(),
                        skills=Skills.query.all(),
                        recaptcha_public=secrets.g_recaptcha_public
                        )

@app.route("/sendmail",methods=["POST"])
def senmdmail():
    data = {"secret": secrets.g_recaptcha_secret,
            "response": request.form.get("token")
            }
    verify = loads(requests.post("https://www.google.com/recaptcha/api/siteverify",data=data).content)["success"]
    if verify == False:
        return {'message': 'Recaptcha Failed. Please try again.'}
    
    if mailsend(request.form.get("subject"),request.form.get("message"),request.form.get("email")):
        return {'message': 'Message has been sent'}
    else:
        return {'message': 'Message could not be sent.'}
        
if __name__ == "__main__":
    app.run("0.0.0.0",8080, debug=True)
