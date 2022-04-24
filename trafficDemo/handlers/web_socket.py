import tornado.websocket
import json
import threading
import serial
import asyncio

serialPort = "com6"
baudRate = 9600

# 串口
# 波特率
ser = serial.Serial(serialPort, baudRate, timeout=0.5)
print("参数设置：串口=%s ，波特率=%d" % (serialPort, baudRate))

class SocketHandler(tornado.websocket.WebSocketHandler):

    clients = set()

    def on_message(self, message):

        print(message)

        data = json.loads(message)
        type = data['type']

        #接收到车流量信息
        if type == 'lane':
            #发送给推理机处理
            reasonHandler(data)

        #接收到信号灯状态信息，转发给下位机
        else:
            state = data['state']
            ser.write(str(state).encode())

    def open(self):

        SocketHandler.clients.add(self)

    def on_close(self):

        SocketHandler.clients.remove(self)

    def check_origin(self, origin):

        return True  # 允许WebSocket的跨域请求

default_handlers = [
    (r"/chat", SocketHandler),
]


'''
    根据前台地图车流量数据进行推理，得出四个状态信号灯的时长，最后返回给前台地图
'''
def reasonHandler(data):

    cars = data['cars']
    topRight = cars["topRight"]
    eastLeft = cars["eastLeft"]
    eastRight = cars["eastRight"]
    topLeft = cars["topLeft"]

    print("topLeft:"+str(topLeft)+ ";topRight:"+str(topRight)+";eastLeft="+str(eastLeft)+";eastRight="+str(eastRight))

    ####################推理机处理逻辑开始#################



    ####################推理机处理逻辑结束#################

    #推理机推理结果
    topRight = 10
    eastLeft = 10
    eastRight = 10
    topLeft = 10

    intersectionLightTimes=[topRight,eastLeft,eastRight,topLeft]

    print(intersectionLightTimes)
    for client in SocketHandler.clients:
        client.write_message(json.dumps({
                'type': "lightTime",
                "data":intersectionLightTimes
            }))


def checkTask():
    last = ""
    while(1):
        data = ser.readline()
        s3 = data.decode().rstrip()
        if s3 == '' and last != '':
            for client in SocketHandler.clients:
                client.write_message(json.dumps({
                    'type': "addCar",
                    "data":True
                }))
        last = s3

def loopCheckTask():
    # loop = asyncio.get_event_loop()  用这种会出现下面报错  使用apscheduler + asyncio 建议使用以下方式
    # 处理报错  RuntimeError: There is no current event loop in thread 'ThreadPoolExecutor-0_0'.
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    bj = loop.create_task(checkTask())
    loop.run_until_complete(asyncio.wait([bj]))

try:
    thread = threading.Thread(target=loopCheckTask)
    thread.start()

except:
   print("Error: unable to start thread")

