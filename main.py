from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy
import models
from db import secrets
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db/portfolio.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


@app.route("/", methods=["GET"])
def index():
    if request.method == "POST":
        pass
    else:
        return render_template("index.html",
                            title="Portfolio of Jan Peterhänsel",
                            technologies=models.Technologies.query.all(),
                            projects=models.Projects.query.all(),
                            skills=models.Skills.query.all(),
                            )

if __name__ == "__main__":
    app.run("0.0.0.0",8080, debug=True)