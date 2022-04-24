
import orm

def addUser(db,username):
    user = orm.User(name=username)
    db.add(user)
    db.commit()

def updateUser(db,id,username):

    user = orm.User.findById(db,id)
    user.name = username
    db.commit()

def deleteUser(db,id):

    user = orm.User.findById(db,id)
    db.delete(user)
    db.commit()

def findUserList(db):

    users = db.query(orm.User).all()
    return users

def addCar(db,carlight,cartraffic,cartime):
    car = orm.Car(light=carlight,traffic=cartraffic,time=cartime)
    db.add(car)
    db.commit()

def updateCar(db,id,carlight,cartraffic,cartime):
    car = orm.Car.findById(db, id)
    car.light = carlight
    car.traffic = cartraffic
    car.time = cartime
    db.commit()

def deleteCar(db, id):
    car=orm.Car.findById(db,id)
    db.delete(car)
    db.commit()


def findCarList(db):
    cars=db.query(orm.Car).all()
    return cars

