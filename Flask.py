import paho.mqtt.client as mqtt
import time
from flask import Flask

app = Flask("Pacote_Teste")
import json

#Servidor Flask que estará enviando o estado para o MQTT.

@app.route('/<string:stat>/<string:mystring>:<int:Id>/<int:myint>')
def combinedroute(stat, mystring, Id, myint):
    def Generator(num): # num se refere ao número de reclosers
        clientes = []
        for i in range (num):
            clientes.append("cliente"+str(i))
            clientes[i] = mqtt.Client(str(i))
        return clientes
    if stat == "Chave" or stat == "state" or stat =="Voltage":
        if mystring == "Id":
            if myint==1:State = True
            else: State = False
            with open("JsonFlask.json", "r") as jsonFile:
                data = json.load(jsonFile)
            Reclosers = data["Recloser"]
            Reclosers[Id][stat] = State
            with open("JsonFlask.json", "w") as jsonFile:
                json.dump(data, jsonFile)
            Cliente = Generator(18)
            Cliente[Id].connect("127.0.0.1")
            Cliente[Id].loop_start()
            Cliente[Id].publish("Changing", str(stat)+"/"+str(myint)+"/Client:" +str(Id))
            time.sleep(1)
            Cliente[Id].loop_stop()

            return ("Client: " + str(Id) + " Changed " + str(stat) + " To:" + str(State))   
    else:
        return "Error"



app.run(host = '127.0.0.1', port = '5000')

