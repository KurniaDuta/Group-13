from flask import Flask, jsonify
from flask_mysqldb import MySQL
from flask import request
import time
import datetime
app = Flask(__name__)
# Required
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = "Elco1001"
app.config["MYSQL_DB"] = "ino"

def fetch(query):
    cur = mysql.connection.cursor()
    cur.execute(query)
    rv = cur.fetchall()
    return jsonify(rv)

mysql = MySQL(app)

@app.route("/all", methods= ['GET'])
def users():
   return fetch("SELECT * FROM temba")

@app.route("/temperatur", methods= ['GET'])
def temp():
   return fetch("SELECT temperatur FROM temba")

@app.route("/kelembaban", methods= ['GET'])
def hum():
   return fetch("SELECT kelembaban FROM temba")

@app.route("/latelest", methods= ['GET'])
def latelest():
    cur = mysql.connection.cursor()
    cur.execute("SELECT COUNT(temperatur) FROM temba")
    count = cur.fetchone()[0] - 1
    cur.execute(f"SELECT * FROM temba limit {count},1")
    rv = cur.fetchone()
    return jsonify(rv)

@app.route("/data", methods=['GET'])
def data(): 
    localtime = time.localtime(time.time())
    hour = str(localtime.tm_hour) + str(localtime.tm_min)
    curTime = int(hour)
    date = datetime.datetime(localtime.tm_year, localtime.tm_mon, localtime.tm_mday)
    cur = mysql.connection.cursor()
    cur.execute(f"SELECT AVG(suhu) FROM data_suhu WHERE kode = (SELECT kode FROM data_suhu WHERE jam <= {curTime} AND hari = '{date.strftime("%A")}' GROUP BY kode ORDER BY MAX(jam) DESC LIMIT 1)")
    kode = cur.fetchone()
    if kode == None :
        return jsonify(kode)
    elif kode[0] == None :
        return jsonify(kode[0])
    else :
        return jsonify(kode)

@app.route("/sendf",methods=['POST'])
def sendfilet():
    try :
        cursor = mysql.connection.cursor()
        data = request.json
        temp = data.get('temp')
        hum = data.get('hum')
        sql = ""
        if temp == None :
            sql = f"INSERT INTO temba VALUES (0, {hum})"
        elif hum == None :
            sql = f"INSERT INTO temba VALUES ({temp}, 0)"
        else :
            sql = f"INSERT INTO temba VALUES ({temp}, {hum})"
        cursor.execute(sql)
        mysql.connection.commit()
        cursor.close()
        return f"{temp}, {hum}"
    except Exception as e:
        return f"Error: {str(e)}"


if __name__ == "__main__":
    app.run(host='0.0.0.0')