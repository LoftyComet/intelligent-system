
import tornado.web
import tornado.ioloop
import json
import orm
import dbUtil
import numpy as np

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
            # 对模糊矩阵进行更新
            # 条件向量
            veryLittle=np.mat('1 0.5 0 0 0')  # 1*5的矩阵
            little=np.mat('0.3 1 0.3 0 0')
            middle=np.mat('0 0.3 1 0.3 0')
            much=np.mat('0 0 0.3 1 0.3')
            veryMuch=np.mat('0 0 0 0.5 1')
            condition_list=condition.split("，")
            condition_array0=[]
            condition_array1=[]
            # 条件一
            if(condition_list[0]=="当前路口车流量极多"):
                condition_array0=veryMuch
            elif(condition_list[0]=="当前路口车流量较多"):
                condition_array0=much
            elif (condition_list[0] == "当前路口车流量适中"):
                condition_array0 = middle
            elif (condition_list[0] == "当前路口车流量较少"):
                condition_array0 = little
            elif (condition_list[0] == "当前路口车流量极少"):
                condition_array0 = veryLittle
            # 条件二
            if (condition_list[1] == "临近路口车流量极多"):
                condition_array1 = veryMuch
            elif (condition_list[1] == "临近路口车流量较多"):
                condition_array1 = much
            elif (condition_list[1] == "临近路口车流量适中"):
                condition_array1 = middle
            elif (condition_list[1] == "临近路口车流量较少"):
                condition_array1 = little
            elif (condition_list[1] == "临近路口车流量极少"):
                condition_array1 = veryLittle
            condition_array=np.dot(condition_array0.T,condition_array1)
            condition_array=condition_array.reshape(1,25)  # 展开  1*25
            # dbUtil.deleteFKnowledge(db,0)
            dbfuzzyMatrix=dbUtil.findFuzzyMatrixById(db,1)
            if (dbfuzzyMatrix== None):
                print("ssssssssssssssssssssssssssssssssss")
                fuzzyMatrix=np.zeros((25,5))
                dbUtil.addFuzzyMatrix(db, " ")

            else:
                dbfuzzyMatrixList=dbfuzzyMatrix.matrix.split(" ")
                for i in dbfuzzyMatrixList:
                    i=float(i)
                fuzzyMatrix=np.matrix(dbfuzzyMatrixList)
                fuzzyMatrix=fuzzyMatrix.reshape((25,5))
                # fuzzyMatrix=np.mat(dbfuzzyMatrix.matrix)   # 同行空格隔开，不同行分号隔开

            # 结论
            verySmall=np.mat('1 0.5 0 0 0')
            small=np.mat('0.3 1 0.3 0 0')
            equal = np.mat('0 0.3 1 0.3 0')
            large = np.mat('0 0 0.3 1 0.3')
            veryLarge = np.mat('0 0 0 0.5 1')
            conclusion_array=[]
            if (conclusion == "红灯与绿灯之比很大" or conclusion=="等待比例很大"):
                conclusion_array = veryLarge
            elif (conclusion == "红灯与绿灯之比较大" or conclusion=="等待比例较大"):
                conclusion_array = large
            elif (conclusion == "红灯与绿灯之比均衡" or conclusion=="等待比例均衡"):
                conclusion_array = equal
            elif (conclusion == "红灯与绿灯之比较小" or conclusion=="等待比例较小"):
                conclusion_array = small
            elif (conclusion == "红灯与绿灯之比很大" or conclusion=="等待比例很小"):
                conclusion_array = verySmall

            addMatrix=np.dot(condition_array.T,conclusion_array)   # 25*5
            fuzzyMatrix=fuzzyMatrix.astype('float64')
            addMatrix=addMatrix.astype('float64')
            fuzzyMatrix=np.maximum(fuzzyMatrix,addMatrix)
            newMatrixStr=""
            for i in range(fuzzyMatrix.shape[0]):
                for j in range(fuzzyMatrix.shape[1]):
                    if(i==0 and j==0):
                        newMatrixStr+=str(fuzzyMatrix[i,j])
                    else:
                        newMatrixStr += " "
                        newMatrixStr+=str(fuzzyMatrix[i,j]) 
                # newMatrixStr+=" "
            
            
            dbUtil.updateFuzzyMatrix(db, 1, newMatrixStr)
            
            # if (dbfuzzyMatrix== None):
            #     print("newMatrixStr-----------------------------------")
            #     print(newMatrixStr)
            #     dbUtil.addFuzzyMatrix(db, newMatrixStr)
            # else:
            #     dbUtil.updateFuzzyMatrix(db, 0, newMatrixStr)
            #     print("newMatrixStr")
            #     print(newMatrixStr)


        elif type == 'edit':
            id=self.get_argument("id");
            condition = self.get_argument("condition")
            conclusion = self.get_argument("conclusion")
            threshold_str = self.get_argument("threshold")
            updater = self.get_argument("updater")
            updateTime = self.get_argument("updateTime")
            # print("threshold")
            # print(threshold_str)
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
