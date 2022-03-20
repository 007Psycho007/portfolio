from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy

import models
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db/portfolio.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)



@app.route("/")
def index():
    return render_template("index.html",
                           title="Portfolio of Jan Peterhänsel",
                           technologies=models.Technologies.query.all(),
                           projects=models.Projects.query.all(),
                           skills=models.Skills.query.all()
                           )

@app.route("/project")
def project():
    print(models.Skills.query.all())
    return render_template("test.html",skills=models.Skills.query.all())

if __name__ == "__main__":
    app.run("0.0.0.0",8080)