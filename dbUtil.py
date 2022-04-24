
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


# 车流量的增删改查
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


# 路口红绿灯时间设计记录的增删改查
def addCrossing(db, cId,topRight,eastLeft,eastRight,topLeft):
    crossing=orm.Crossing(cId=cId,topRight=topRight,eastLeft=eastLeft,eastRight=eastRight,topLeft=topLeft)
    db.add(crossing)
    db.commit()
def updateCrossing(db, id,cId,topRight,eastLeft,eastRight,topLeft):
    crossing = orm.Crossing.findById(db, id)
    crossing.cId=cId
    crossing.topRight=topRight
    crossing.topLeft=topLeft
    crossing.eastLeft=eastLeft
    crossing.eastRight=eastRight;
    db.commit()
def deleteCrossing(db, id):
    crossing=orm.Crossing.findById(db,id)
    db.delete(crossing)
    db.commit()
def findCrossingList(db):
    crossings=db.query(orm.Crossing).all()
    return crossings

# 路口ID对于信号灯ID的对应
def addCLight(db, cId, light,direction):
    clight=orm.CLight(cId=cId, light=light, direction=direction)
    db.add(clight)
    db.commit()

def updateCLight(db, cId, light,direction):
    clight=orm.CLight.findbyLight(light)
    clight.cId=cId;
    clight.direction=direction
    db.commit()
def deleteCLight(db, light):
    clight=orm.CLight.findById(db,light)
    db.delete(clight)
    db.commit()
def findCLightList(db):
    clights=db.query(orm.CLight).all()
    return clights


