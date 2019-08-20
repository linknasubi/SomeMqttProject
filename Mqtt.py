import paho.mqtt.client as mqtt
import time
import json

class Reclosers:
    

#    Reclosers que estão enviando seus estados a partir da leitura de um arquivo json.
#    Estes devem armazenar seus estados atuais em um arquivo json gerado pelo próprio código. 
    
    def __init__(self):
        self.num = 18
        
    def createJSON(self):
        with open ("Teste4.json", "w") as outfile:
            List = []
            for _ in range (self.num):
                Recloser = ([{"Id": str(_), "Chave": False, "Voltage": 0, "state": False, "waiting_state_change": False, "waiting_voltage_change": False}])
                List.append(Recloser)
            json.dump(List, outfile)

    def getJSON(self):
        with open("Teste4.json", 'r') as fp:
            return json.load(fp)
        
    def Generator(self): # Gera os objetos cliente.
        self.clientes = []
        for i in range (self.num):
            self.clientes.append("cliente"+str(i))
            self.clientes[i] = mqtt.Client(str(i))
        return self.clientes
    
            
    
    def Rep(self): # Realiza o envio dos estados dos religadores
        a = -1
        while True:
            for _ in self.clientes:
                a += 1
                self.myObj = self.getJSON()
                #self.recloser = self.myObj["Recloser"]
                obj = self.myObj[a]
                _.connect("127.0.0.1")
                _.loop_start()
                _.publish("Topic_"+str(a),"Message:"+str(obj)+" From Client "+str(a))
                _.loop_stop()
            a = -1
            time.sleep(10)
        
Teste = Reclosers()
methods = [Teste.__init__(), Teste.createJSON(), Teste.getJSON(), Teste.Generator(),Teste.Rep()]
for _ in methods:
    _

            
