from flask import Flask

app = Flask(__name__)

@app.route('/')
def dashboard():
    return "<h1>Telemetry Dashboard</h1>"
 