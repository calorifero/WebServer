from .main import db

# this function is used to test API, it will be modified


def init_database():
    from .models import EspModel, TemperatureModel
    db.drop_all()
    db.create_all()
    mac = EspModel(mac_address='2b:fe:c3:92:b5:a8')
    db.session.add(mac)
    mac = EspModel(mac_address='37:22:04:14:2b:52')
    db.session.add(mac)
    mac = EspModel(mac_address='47:70:b8:ee:86:b5')
    db.session.add(mac)
    temp = TemperatureModel(temperature=34.12, esp='2b:fe:c3:92:b5:a8')
    db.session.add(temp)
    temp = TemperatureModel(temperature=14.12, esp='37:22:04:14:2b:52')
    db.session.add(temp)
    temp = TemperatureModel(temperature=4.2, esp='47:70:b8:ee:86:b5')
    db.session.add(temp)
    db.session.commit()
