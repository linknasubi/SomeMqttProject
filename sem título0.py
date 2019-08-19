import paho.mqtt.client as mqtt
import time
import json

def getJSON(filePathAndName):
    with open(filePathAndName, 'r') as fp:
        return json.load(fp)
    
def Gener(num):
    clientes = []
    for i in range (num):
        clientes.append("cliente"+str(i))
        clientes[i] = mqtt.Client(str(i))
    return clientes

clientes = Gener(5)

def Rep(clientes):
    a = -1
    while True:
        for _ in clientes:
            myObj = getJSON('./Teste3.json')
            recloser = myObj.get("Recloser")
            a += 1
            obj = recloser[a]
            _.connect("127.0.0.1")
            _.loop_start()
            _.publish("Topic","Message:"+str(obj)+" From Client "+str(a))
            _.loop_stop()
        a = -1
        time.sleep(10)
        
Teste = Rep(clientes)
            
