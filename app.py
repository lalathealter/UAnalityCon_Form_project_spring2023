import os
from flask import Flask
from flask import request, render_template
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv

load_dotenv()
USERNAME=os.getenv('USERNAME')
PASSWORD=os.getenv('PASSWORD')
HOST=os.getenv('HOST')
PORT=os.getenv('PORT')
DATABASE_NAME=os.getenv('DATABASE_NAME')

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = \
    'mysql://{0}:{1}@{2}:{3}/{4}'.format(
    USERNAME, PASSWORD, HOST, PORT, DATABASE_NAME 
)

# db = SQLAlchemy(app)

@app.route("/", methods=['GET', 'POST'])
def form():
    if request.method == "POST":
        
        data = (request.form.to_dict(flat=False))
        print(data)
        # save_visitor_data(data)
        return render_template("accept.html")
    else:
        return render_template("form.html")


# def save_visitor_data(datadict: dict):
#     vdata = VisitorData(datadict)
#     db.session.add(vdata)
#     db.session.commit()

# TINY = 16
# SMALL = 128
# BIG = 2048
# class VisitorData():
#     id = db.Column(db.Integer, primary_key=True)

#     fname_russian = db.Column(db.String(SMALL), nullable=False)
#     lname_russian = db.Column(db.String(SMALL), nullable=False)
#     patronym_russian = db.Column(db.String(SMALL))
#     email = db.Column(db.String(SMALL), nullable=False)
    
#     acad_degree_russian =  db.Column(db.String(SMALL), nullable=False)
#     acad_rank_russian = db.Column(db.String(SMALL), nullable=False)
#     phone_number = db.Column(db.String(TINY), nullable=False)
#     fname_english =  db.Column(db.String(SMALL), nullable=False)
#     lname_english =  db.Column(db.String(SMALL), nullable=False)

#     place_of_work_english =  db.Column(db.String(SMALL), nullable=False)
#     position_english =  db.Column(db.String(SMALL), nullable=False)
#     acad_degree_english =  db.Column(db.String(SMALL), nullable=False)
#     acad_rank_english =  db.Column(db.String(SMALL), nullable=False)

#     report_name_russian =  db.Column(db.String(SMALL), nullable=False)
#     report_name_english =  db.Column(db.String(SMALL), nullable=False)
#     coauthors_info =  db.Column(db.String(BIG))
#     report_thesis =  db.Column(db.String(BIG), nullable=False)
#     report_type = db.Column(db.String(TINY), nullable=False)
#     def __init__(self, dictionary):
#          for k, v in dictionary.items():
#             setattr(self, k, v)
