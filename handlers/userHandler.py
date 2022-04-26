
import tornado.web
import tornado.ioloop
import json
import orm
import dbUtil

class UserHandler(tornado.web.RequestHandler):

    def post(self, *args, **kwargs):
        db = self.settings['db']
        dic = {"status":True,"message":""}
        type = self.get_argument("type")
        if type == 'add':
            username = self.get_argument("username")
            print(username)
            dbUtil.addUser(db,username)
        elif type == 'edit':
            id = self.get_argument("id")
            username = self.get_argument("username")
            print(username)
            dbUtil.updateUser(db,id,username)
        elif type == 'delete':
            id = self.get_argument("id")
            dbUtil.deleteUser(db,id)

        self.write(json.dumps(dic))

    def get(self, *args, **kwargs):
        self.render("index.html")



class CarHandler(tornado.web.RequestHandler):

    def post(self, *args, **kwargs):
        db = self.settings['db']
        dic = {"status":True,"message":""}
        type = self.get_argument("type")
        if type == 'add':
            carlight = self.get_argument("light")
            cartraffic = self.get_argument("traffic")
            cartime = self.get_argument("time")
            # print("carname")
            print(cartime)
            dbUtil.addCar(db,carlight,cartraffic,cartime)
        elif type == 'edit':
            id=self.get_argument("id");
            carlight = self.get_argument("light")
            cartraffic = self.get_argument("traffic")
            cartime = self.get_argument("time")
            dbUtil.updateCar(db,id,carlight,cartraffic,cartime)
        elif type == 'delete':
            id = self.get_argument("id")
            dbUtil.deleteCar(db,id)

        self.write(json.dumps(dic))

    def get(self, *args, **kwargs):
        self.render("index.html")


class FKnowledgeHandler(tornado.web.RequestHandler):

    def post(self, *args, **kwargs):
        db = self.settings['db']
        dic = {"status":True,"message":""}
        type = self.get_argument("type")
        if type == 'add':
            condition = self.get_argument("condition")
            conclusion = self.get_argument("conclusion")
            threshold_str = self.get_argument("threshold")
            updater = self.get_argument("updater")
            updateTime = self.get_argument("updateTime")
            threshold=float(threshold_str)
            dbUtil.addFKnowledge(db,condition, conclusion, threshold, updater, updateTime)
        elif type == 'edit':
            id=self.get_argument("id");
            condition = self.get_argument("condition")
            conclusion = self.get_argument("conclusion")
            threshold_str = self.get_argument("threshold")
            updater = self.get_argument("updater")
            updateTime = self.get_argument("updateTime")
            print("threshold")
            print(threshold_str)
            threshold = float(threshold_str)
            dbUtil.updateFKnowledge(db,id,condition, conclusion, threshold, updater, updateTime)
        elif type == 'delete':
            id = self.get_argument("id")
            dbUtil.deleteFKnowledge(db,id)

        self.write(json.dumps(dic))

    def get(self, *args, **kwargs):
        self.render("index.html")

default_handlers = [
    (r"/user", UserHandler),
    (r"/car", CarHandler),
    (r"/rule", FKnowledgeHandler),
]
