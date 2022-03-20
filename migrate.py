import models
from models import db
import os
os.remove('db/portfolio.db')
db.create_all()

# Projects
long_description = """This is a demo password manager using Python as underlying language. 
It use SHA256 to Hash the Userpassword and uses AES 256 to securely encrypt the password entries. 
To store the data it uses a SQLite database backend. The whole project is designed in OOP.
As frontend it uses a standard Tkinter GUI """
db.session.add(models.Projects(type="Personal",name="Password Manager",description="Password Manager using AES Encrytption",long_description=long_description,url="https://github.com",used_technologies="Python,tkinter"))

long_description = """This demo project can shorten long urls to to shorter urls. 
It uses Flask as Web Framework and pico.css as a Frontend Framework. 
As database it uses a SQLite Backend """
db.session.add(models.Projects(type="Personal",name="URL Shorter",description="URL Shortener using Flask",long_description=long_description,url="https://github.com",used_technologies="Python,Flask,pico.css"))

# Technologies
db.session.add(models.Technologies(name="Python",level=100))
db.session.add(models.Technologies(name="Flask",level=80))
db.session.add(models.Technologies(name="Django",level=60))
db.session.add(models.Technologies(name="MySQL",level=60))
db.session.add(models.Technologies(name="Bash",level=80))
db.session.add(models.Technologies(name="HTML & CSS",level=60))
db.session.add(models.Technologies(name="Git",level=60))
db.session.add(models.Technologies(name="C++",level=40))

#Skills
db.session.add(models.Skills(name="Linux",short_desc="Experience in managing and administrating Linux Servers"))
db.session.add(models.Skills(name="Web Development",short_desc="Experience in combining Web Languages like HTML, CSS, JS and Python to build Web Apps"))
db.session.add(models.Skills(name="Data Structures",short_desc="Understanding of different data structures like Arrays, Hashmaps and Graphs"))
db.session.add(models.Skills(name="Algorithm Design",short_desc="Understanding of algorithms like search and sorting algorithms and the ability to apply these principals"))
db.session.add(models.Skills(name="Database Design and Operation",short_desc="Understanding of database design and operation like nomalization,Foreign Keys, etc."))
db.session.add(models.Skills(name="Data Analysis",short_desc="Experience with analysis data with Python, pandas, numpy, etc. with focus of getting the requested values from the data. This includes, Cleaning, Exploring and Visualising. "))
db.session.add(models.Skills(name="Cryptography",short_desc="Experience with using cryptographical algorithms like hashes, encryption and certificates."))
db.session.add(models.Skills(name="Object Oriented Design",short_desc="Experience with applying "))
db.session.commit()

