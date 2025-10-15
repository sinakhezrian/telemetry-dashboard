import os
from dotenv import load_dotenv 
from flask import Flask, render_template

load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config['DATABASE_URL'] = os.getenv('DATABASE_URL')  

@app.route('/')
def dashboard():
    return render_template('dashboard.html')
 