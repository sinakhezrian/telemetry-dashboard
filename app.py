import os
from datetime import datetime
from dotenv import load_dotenv 
from flask_migrate import Migrate
from flask import Flask, render_template, request
from models import db, Telemetry
from sqlalchemy import text
from flask_socketio import SocketIO, emit



load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")

db.init_app(app)
migrate = Migrate(app, db)

socketio = SocketIO(app, cors_allowed_origins="*")

@socketio.on('connect')
def handle_connect():
    emit('connect')
    print('Client connected')


@socketio.on('disconnect')
def handle_disconnect():
    emit('disconnect')
    print('Client disconnected')


@app.route('/db-connection-test')
def db_connection_test():
    try:
        db.session.execute(text('SELECT 1'))
        return render_template('database-status.html', status="success")
    except Exception:
        return render_template('database-status.html', status="failed")

@app.route('/')
def dashboard():
    telemetries = Telemetry.query.order_by(Telemetry.created_at.desc()).limit(10).all()
    return render_template('dashboard.html', telemetries=telemetries)


@app.route("/telemetry", methods=["POST"])
def receive_telemetry():
    data = request.get_json()
    
    # Validation ------>
    if not data:
        return {"error": "No data provided"}, 400
    
    if "sensor" not in data:
        return {"error": "Sensor name is reqired"}, 400
    elif "value" not in data:
        return {"error": "Value is reqired"}, 400
    
    sensor_name = data.get("sensor")
    time_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    try:
        for key, val in data.items():
            if key in ["created_at", "sensor"]:
                continue
            
            try:
                value = float(val)
            except (ValueError, TypeError):
                return {"error": f"Invalid value for {key}: {val}"}, 400
            
            entry = Telemetry(
                sensor=sensor_name,
                value=value,
                created_at=time_str
            )
            db.session.add(entry)
        
        db.session.commit()
        
        socketio.emit('new_data', {
            'sensor': sensor_name,
            'value': value,
            'time': time_str
        })
        
        return {"status": "success"}, 200  
    except Exception as e:
        db.session.rollback()
        return {"error": f"Database error: {str(e)}"}, 500

 
 
if __name__ == '__main__':
    with app.app_context():
         db.create_all()
    socketio.run(app, debug=True, host="0.0.0.0", port=5000)
