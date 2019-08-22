import paho.mqtt.client as mqtt
import time
import json
#from Listener import createJSON, Rep

num = 18
global pyld
pyld = "Chave/0/Client:0"
def on_message(client, userdata, message): #Callback para ouvir a mensagem que chega ao tópico enviado pelo servidor flask.
    global pyld
    pyld = "Chave/0/Client:0"
    pyld = str((message.payload.decode('UTF-8')))
    print(pyld)


def createJSON(): #Criação do arquivo json a ser utilizado.
    with open ("JsonClient.json", "w") as outfile:
        List = []
        for _ in range (num):
            Recloser = ({"Id": str(_), "Chave": False, "Voltage": 0, "state": False, "waiting_state_change": False, "waiting_voltage_change": False})
            List.append(Recloser)
        json.dump(List, outfile)


def getJSON(): #Leitura do arquivo json.
    with open("JsonClient.json", 'r') as fp:
        return json.load(fp)
    
def Generator(): # Gera os objetos cliente.
    clientes = []
    for i in range (num):
        clientes.append("cliente"+str(i))
        clientes[i] = mqtt.Client(str(i))
        clientes[i].on_message = on_message
    return clientes

gen = Generator()

def Rep(): # Escuta, Modifica, Lê e Publica o estado dos religadores respectivamente.
    a = -1
    while True:
        for _ in gen:
            #Tratamento das mensagens do Recloser
            if pyld[-10]=="1":State = True
            else: State = False
            Sub = (len(pyld)) - 11 
            Id = int(pyld[-1])
            newpyld = pyld[0:(Sub)]
            #-----------------------------------
            a += 1
            myObj = getJSON()
            objL = myObj[Id]
            objL[newpyld] = State
            objP = myObj[a]     
            with open("JsonClient.json", "w") as jsonFile:
                json.dump(myObj, jsonFile)
            _.connect("127.0.0.1", port = 1883)
            _.loop_start()
            _.subscribe("Changing", qos=2)
            _.publish("Topic_"+str(a),"Message:"+str(objP)+" From Client "+str(a))
            time.sleep(0.1)
            _.loop_stop()
        a = -1
    
createJSON()
Rep()
