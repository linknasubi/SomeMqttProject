import paho.mqtt.client as mqtt
import time
from flask import Flask, render_template
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
    if stat == ("Chave" or "state" or "Voltage"):
        if mystring == "Id":
            if myint==1:State = True
            else: State = False
            with open("teste3.json", "r") as jsonFile:
                data = json.load(jsonFile)
            Reclosers = data["Recloser"]
            Reclosers[Id][stat] = State
            with open("teste3.json", "w") as jsonFile:
                json.dump(data, jsonFile)
            Cliente = Generator(18)
            Cliente[Id].connect("127.0.0.1")
            Cliente[Id].loop_start()
            Cliente[Id].publish("Changing_"+str(Id), str(stat)+"/"+str(myint))
            time.sleep(1)
            Cliente[Id].loop_stop()  
            
            return "AAAAA"   
    else:
        return "Error"



app.run(host = '127.0.0.1', port = '5000')
