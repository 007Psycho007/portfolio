from flask import Flask, request, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy
import models
from db import secrets 
import requests
from json import loads
import smtplib, ssl
from db import secrets
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db/portfolio.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

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
                        technologies=models.Technologies.query.all(),
                        projects=models.Projects.query.all(),
                        skills=models.Skills.query.all(),
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