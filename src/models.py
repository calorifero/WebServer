from .database import db


class EspModel(db.Model):
    __tablename__ = 'Esp'
    mac_address = db.Column(db.String(17), primary_key=True)
    rel = db.relationship('TemperatureModel', backref='EspModel')


class TemperatureModel(db.Model):
    __tablename__ = 'Temperature'
    id_temp = db.Column(db.Integer, db.Sequence('temp_id_seq'), primary_key=True)
    temperature = db.Column(db.Numeric(4, 2), )
    esp = db.Column(db.String(17), db.ForeignKey(EspModel.mac_address), )
