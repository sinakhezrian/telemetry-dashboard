from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()   

class Telemetry(db.Model):
    __tablename__ = 'telemetry'
    id = db.Column(db.Integer, primary_key=True)
    sensor = db.Column(db.String(50), nullable=False)
    value = db.Column(db.Float, nullable=False)
    created_at = db.Column(db.String(50), nullable=False)
    
    def __repr__(self):
        return f"<Telemetry(sensor={self.sensor}, value={self.value}, created_at={self.created_at})>"
    
    def to_dict(self):
        return {
            'id': self.id,
            'sensor': self.sensor,
            'value': self.value,
            'created_at': self.created_at
        }
        