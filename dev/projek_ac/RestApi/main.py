from flask import Flask, request, jsonify, json
from threading import Thread
from flask_cors import cross_origin
from room import lt5, lt6, lt7, lt8
from information import result
from to_ino import result_datas

app = Flask(__name__)

temp = [['on' for _ in range(16)] for _ in range(4)]
person = [[1 for _ in range(16)] for _ in range(4)]
temperature = [["28" for _ in range(16)] for _ in range(4)]

ino = {
    'kode' : 'h',
    'index1' : '0',
    'index2' : '5'
}

lantai5 = lt5(person[0], temp[0], temperature[0])
lantai6 = lt6(person[1], temp[1], temperature[1])
lantai7 = lt7(person[2], temp[2], temperature[2])
lantai8 = lt8(person[3], temp[3], temperature[3])
info = result(lantai5, lantai6, lantai7, lantai8)

@app.route('/person', methods=['POST'])
@cross_origin()
def update_count_in():
    global person, lantai5
    data = request.json
    person[0][0] = data.get('person')
    lantai5 = lt5(person[0], temp[0], temperature[0])
    return person

@app.route('/information', methods=['GET'])
@cross_origin()
def get_information():
    global ino
    ino = result_datas(lantai5[0]['kode'], lantai5[0]['suhu'], lantai5[0]['standar'], lantai5[0]['status'], person[0][0], ino['index2'])
    return jsonify(ino)

@app.route('/temperature', methods=['POST'])
@cross_origin()
def post_temperature():
    global lantai5
    data = request.json
    temperature[0][0] = data.get('temp')
    temperature[0][0] = int(float(temperature[0][0]))
    lantai5 = lt5(person[0], temp[0], temperature[0])
    return lantai5


@app.route('/info', methods=['GET'])
@cross_origin()
def post_information():
    global info
    info = result(lantai5, lantai6, lantai7, lantai8)
    return jsonify(info)

@app.route('/floor5p', methods=['POST'])
@cross_origin()
def post_floor5():
    global lantai5
    data = request.json
    for i in range(len(lantai5)) :
        temp[0][i] = data[i].get('status')
    lantai5 = lt5(person[0], temp[0], temperature[0])
    return lantai5

@app.route('/floor5g', methods=['GET'])
@cross_origin()
def get_floor5():
    global lantai5
    return jsonify(lantai5)

@app.route('/floor6p', methods=['POST'])
@cross_origin()
def post_floor6():
    global lantai6
    data = request.json
    for i in range(len(lantai6)) :
        temp[1][i] = data[i].get('status')
    lantai6 = lt6(person[1], temp[1], temperature[1])
    return lantai6

@app.route('/floor6g', methods=['GET'])
@cross_origin()
def get_floor6():
    global lantai6
    return jsonify(lantai6)

@app.route('/floor7p', methods=['POST'])
@cross_origin()
def post_floor7():
    global lantai7
    data = request.json
    for i in range(len(lantai7)) :
        temp[2][i] = data[i].get('status')
    lantai7 = lt7(person[2], temp[2], temperature[2])
    return lantai7

@app.route('/floor7g', methods=['GET'])
@cross_origin()
def get_floor7():
    global lantai7
    return jsonify(lantai7)

@app.route('/floor8p', methods=['POST'])
@cross_origin()
def post_floor8():
    global lantai8
    data = request.json
    for i in range(len(lantai8)) :
        temp[3][i] = data[i].get('status')
    lantai8 = lt8(person[3], temp[3], temperature[3])
    return lantai8

@app.route('/floor8g', methods=['GET'])
@cross_origin()
def get_floor8():
    global lantai8
    return jsonify(lantai8)
         
if __name__ == '__main__':
    app.run(host='0.0.0.0')