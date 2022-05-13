'''
Author       : LinMu
Date         : 2022-04-28 21:57:09
FilePath     : \main.py
Description  : 
LastEditors  : LinMu
LastEditTime : 2022-04-29 11:10:03
'''

import numpy as np
from pandas import array

def initMatrix():
    global indoorLight,lightDiffer,lightSpeed,curtains,numPerson
    indoorLight = np.array([[1  ,0.2,0  ,0  ,0  ],
                            [0.2,0.8,0.3,0  ,0  ],
                            [0  ,0.3,0.8,0.3,0  ],
                            [0  ,0  ,0.5,0.8,0.3],
                            [0  ,0  ,0  ,0.5,1  ]])
    lightDiffer = np.array([[1  ,0.3,0  ],
                            [0.3,1  ,0.3],
                            [0  ,0.3,1  ]])
    lightSpeed  = np.array([[0.9,0.5,0  ,0  ],
                            [0.3,0.9,0.3,0  ],
                            [0  ,0.3,0.9,0.3],
                            [0  ,0  ,0.5,0.9]])
    curtains    = np.array([[1  ,0.5,0  ,0  ,0  ],
                            [0.3,1  ,0.3,0  ,0  ],
                            [0  ,0.3,1  ,0.3,0  ],
                            [0  ,0  ,0.5,1  ,0.3],
                            [0  ,0  ,0  ,0.5,1  ]])
    numPerson   = np.array([[1  ,0.5,0  ],
                            [0.2,0.8,0.5],
                            [0  ,0.2,0.8]])

    global fuzzyMap
    fuzzyMap = {"VD":0,"LD":1,"ST":2,"LB":3,"VB":4,
                "BR":0,"EQ":1,"DA":2,
                "FD":0,"SD":1,"SU":2,"FU":3,
                "CC":0,"SO":1,"HO":2,"SC":3,"CO":4,
                "NP":0,"FP":1,"MP":2}
    global matrixMap
    matrixMap ={"室内亮度":indoorLight,"室内外亮度差":lightDiffer,"灯光调节速度":lightSpeed,
                "窗帘开闭程度":curtains,"房间人数":numPerson,
                "VD":indoorLight,"LD":indoorLight,"ST":indoorLight,"LB":indoorLight,"VB":indoorLight,
                "BR":lightDiffer,"EQ":lightDiffer,"DA":lightDiffer,
                "FD":lightSpeed,"SD":lightSpeed,"SU":lightSpeed,"FU":lightSpeed,
                "CC":curtains,"SO":curtains,"HO":curtains,"SC":curtains,"CO":curtains,
                "NP":numPerson,"FP":numPerson,"MP":numPerson}
def countMatrix(i,j):
    array1 = (matrixMap[i])[fuzzyMap[i]]
    array2 = (matrixMap[j])[fuzzyMap[j]]
    xlen = np.size(array1)
    ylen = np.size(array2)
    resMatrix = np.zeros((xlen,ylen))
    for x in range(0,xlen):
        for y in range(0,ylen):
            resMatrix[x][y] = max(min(array1[x],array2[y]),(1-array1[x]))
    return resMatrix
if __name__ == "__main__":
    print("start!!!")
    initMatrix()
    print(countMatrix("CO","FU"))
    # print(np.multiply(indoorLight,curtains))

