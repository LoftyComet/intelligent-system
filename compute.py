from operator import index
import numpy as np
from pandas import array


def getFuzzyVector(input1,input2,fuzzy_matrix):
    """
    根据两个输入决策获取决策结果
    """
    if (input1=="VF"):
        input1 = np.matrix([1,0.5,0,0,0])
    elif (input1=="LF"):
        input1 = np.matrix([0.5,1,0.5,0,0])
    elif (input1=="M"):
        input1 = np.matrix([0,0.5,1,0.5,0])
    elif (input1=="LM"):
        input1 = np.matrix([0,0,0.5,1,0.5])
    elif (input1=="VM"):
        input1 = np.matrix([0,0,0,0.5,1])
    if (input2=="VF"):
        input2 = np.matrix([1,0.5,0,0,0])
    elif (input2=="LF"):
        input2 = np.matrix([0.5,1,0.5,0,0])
    elif (input2=="M"):
        input2 = np.matrix([0,0.5,1,0.5,0])
    elif (input2=="LM"):
        input2 = np.matrix([0,0,0.5,1,0.5])
    elif (input2=="VM"):
        input2 = np.matrix([0,0,0,0.5,1])
    temp = input1.T * input2
    
    result = np.dot(temp.flatten()+0.1,fuzzy_matrix)
    return result

def getVF(car):
    return max(-car/40 + 1, 0)
def getLF(car):
    if (car>20):
        return max(-car/40 + 1.5, 0)
    else:
        return max(0.5+car/40,0)
def getM(car):
    if (car>40):
        return max(-car/40 + 2, 0)
    else:
        return max(car/40,0)
def getLM(car):
    if (car>60):
        return max(-car/40 + 2.5, 0)
    else:
        return max(car/40-0.5,0)
def getVM(car):
    if (car>80):
        return max(-car/40 + 3, 0)
    else:
        return max(car/40-1,0)


def getFuzzyElement(topRight,eastLeft,eastRight,topLeft):
    """
    根据四个方向车流量映射到模糊集元素
    """
    horizon = (eastLeft + eastRight) / 2
    vertical = (topLeft+topRight) / 2
    membership = ["VF","LF","M","LM","VM"]
    horizons=[getVF(horizon),getLM(horizon),getM(horizon),getLM(horizon),getVM(horizon)]
    verticals=[getVF(vertical),getLM(vertical),getM(vertical),getLM(vertical),getVM(vertical)]
    return membership[horizons.index(max(horizons))],membership[verticals.index(max(verticals))]


def getProportion(decision):
    """
    根据决策类型得出时间长度
    """
    decision = decision.tolist()
    decision = decision[0]
    print(decision)
    index = decision.index(max(decision))
    if (index==0):
        return 10,20
    elif (index==1):
        return 12,18
    elif (index==2):
        return 15,15
    elif (index==3):
        return 18,12
    else :
        return 20,10