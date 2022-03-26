from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy
import models
from db import secrets 
import requests
import json
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db/portfolio.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


@app.route("/", methods=["GET","POST"])
def index():
    if request.method == "POST":
        data = {"secret": secrets.g_recaptcha_secret,
                "response": request.form.get("g-recaptcha-response")
                }
        verify = json.loads(requests.post("https://www.google.com/recaptcha/api/siteverify",data=data).content)["success"]
        if verify == True:
            form_response = "Verified"
        else:
            form_response = "Recaptcha failed. Please try again"
    else:
        form_response = False
    
    return render_template("index.html",
                        title="Portfolio of Jan Peterhänsel",
                        form_response = form_response,
                        technologies=models.Technologies.query.all(),
                        projects=models.Projects.query.all(),
                        skills=models.Skills.query.all(),
                        recaptcha_public=secrets.g_recaptcha_public
                        )

if __name__ == "__main__":
    app.run("0.0.0.0",8080, debug=True)