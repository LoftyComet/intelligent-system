def outputEvidence(output1,output2):
    """
    根据车流量输入解释所使用的证据
    """
    currentcar = ""
    nextcar = ""
    if (output1=="VF"):
        currentcar = "当前路口车辆非常多"
    elif (output1=="LF"):
        currentcar = "当前路口车辆比较多"
    elif (output1=="M"):
        currentcar = "当前路口车辆适中"
    elif (output1=="LM"):
        currentcar = "当前路口车辆比较少"
    elif (output1=="VM"):
        currentcar = "当前路口车辆非常少"
    if (output2=="VF"):
        nextcar = "临近路口车辆非常多"
    elif (output2=="LF"):
        nextcar = "临近路口车辆比较多"
    elif (output2=="M"):
        nextcar = "临近路口车辆适中"
    elif (output2=="LM"):
        nextcar = "临近路口车辆比较少"
    elif (output2=="VM"):
        nextcar = "临近路口车辆非常少"
    return currentcar,nextcar


def outputDecision(currenttime,nexttime):
    """
    解释得到的结论
    """
    if (currenttime==10):
        return "当前路口绿灯时间极短" 
    elif(currenttime==12):
        return "当前路口绿灯时间较短"
    elif(currenttime==15):
        return "当前路口绿灯时间适中"
    elif(currenttime==18):
        return "当前路口绿灯时间较长"
    elif(currenttime==20):
        return "当前路口绿灯时间极短"
