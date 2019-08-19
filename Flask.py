from flask import Flask, render_template
app = Flask("Pacote_Teste")
import json

@app.route('/combinedroute/<string:mystring>:<int:Id>/<int:myint>')
def combinedroute(mystring, Id, myint):
    
    if mystring == "Id":   
        if myint==1:State = True
        else: State = False
        with open("teste3.json", "r") as jsonFile:
            data = json.load(jsonFile)
        Reclosers = data["Recloser"]
        Reclosers[Id]["Chave"] = State
        with open("teste3.json", "w") as jsonFile:
            json.dump(data, jsonFile)
        return "AAAAA"   
    else:
        return "Error"


app.run(host = '127.0.0.1', port = '5000')
