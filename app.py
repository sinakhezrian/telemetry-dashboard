import os
from dotenv import load_dotenv 
from flask_migrate import Migrate
from flask import Flask, render_template
from models import db, Telemetry
from sqlalchemy import text


load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")

db.init_app(app)
migrate = Migrate(app, db)


@app.route('/db-connection-test')
def db_connection_test():
    try:
        db.session.execute(text('SELECT 1'))
        return render_template('database-status.html', status="success")
    except Exception:
        return render_template('database-status.html', status="failed")

@app.route('/')
def dashboard():
    return render_template('dashboard.html')
 
 
 
if __name__ == '__main__':
    with app.app_context():
         db.create_all()