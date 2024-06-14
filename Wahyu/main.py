from flask import Flask, jsonify
from flask import request

app = Flask(__name__)
    
temperatur = ""
humidity = ""



@app.route("/data", methods= ['GET'])
def users():
   return f"temperatur : {temperatur}, humidity : {humidity}"


@app.route("/sendf",methods=['POST'])
def sendfilet():
        data = request.json
        global temperatur, humidity
        temperatur = data.get('temp')
        humidity = data.get('hum')
        return "sukses"


if __name__ == "__main__":
    app.run(host='0.0.0.0')