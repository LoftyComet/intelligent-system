
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


# 可信度知识库的增删改查
def addCKnowledge(db, condition, conclusion, threshold, updater, updateTime):
    cknowledge=orm.CKnowledge(condition=condition,
                              conclusion=conclusion,
                              threshold=threshold,
                              updater=updater,
                              updateTime=updateTime)
    db.add(cknowledge)
    db.commit()
def updateCKnowledge(db, id, condition, conclusion, threshold,updater, updateTime):
    cknowledge=orm.CKnowledge.findbyId(db,id)
    cknowledge.condition=condition
    cknowledge.conclusion=conclusion
    cknowledge.threshold=threshold
    cknowledge.updater=updater
    cknowledge.updateTime=updateTime
    db.commit()
def deleteCKnowledge(db, id):
    cknowledge = orm.CKnowledge.findbyId(db, id)
    db.delete(cknowledge)

def findCKnowledgeList(db):
    cknowledges=db.query(orm.CKnowledge).all()
    return cknowledges
def findCKknowledgeById(db, id):
    cknowledge = orm.CKnowledge.findbyId(db, id)
    return cknowledge
def findCKknowledgeByCondition(db, condition):
    cknowledges = orm.CKnowledge.findbyCondition(db, condition)
    return cknowledges

# 模糊知识库的增删改查
def addFKnowledge(db,condition, conclusion, threshold,updater, updateTime):
    fknowledge=orm.FKnowledge(condition=condition,conclusion=conclusion,
                              threshold=threshold, updater=updater, updateTime=updateTime)
    db.add(fknowledge)
    db.commit()
def updateFKnowledge(db, id, condition, conclusion, threshold,updater, updateTime):
    fknowledge=orm.FKnowledge.findbyId(db,id)
    fknowledge.condition=condition
    fknowledge.conclusion=conclusion
    fknowledge.threshold=threshold
    fknowledge.updater=updater
    fknowledge.updateTime=updateTime
    db.commit()
def deleteFKnowledge(db, id):
    fknowledge = orm.FKnowledge.findbyId(db, id)
    db.delete(fknowledge)

def findFKnowledgeList(db):
    fknowledges=db.query(orm.FKnowledge).all()
    return fknowledges
def findFKknowledgeById(db, id):
    fknowledge = orm.FKnowledge.findbyId(db, id)
    return fknowledge
def findFKknowledgeByCondition(db, condition):
    fknowledges = orm.FKnowledge.findbyCondition(db, condition)
    return fknowledges


