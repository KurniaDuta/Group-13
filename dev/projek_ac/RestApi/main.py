import torch
import cv2
from flask import Flask, request, jsonify, json
from threading import Thread
from flask_cors import cross_origin
from room import lantai5, lantai6, lantai7, lantai8

app = Flask(__name__)
# CORS(app)
# cap = cv2.VideoCapture(0)
# model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)
person = 0

lantai5 = lantai5()
lantai6 = lantai6()
lantai7 = lantai7()
lantai8 = lantai8()

info = {
    "fifth" : 'n',
    "sixth" : 'n',
    "seventh" : 'n',
    "eighth" : 'n'
}
temperature_humidity = {
    "temp" : 26,
    "hum" : 26
}

# def video_capture():
#     global person
#     while True:
#         ret, frame = cap.read()
#         if not ret :
#             break
#         results = model(frame)
#         person = 0
#         for _,row in results.pandas().xyxy[0].iterrows():
#             if row['name'] == 'person':
#                 cv2.rectangle(frame, (int(row['xmin']), int(row['ymin'])), (int(row['xmax']), int(row['ymax'])), (255, 0, 0))
#                 person += 1
#         cv2.imshow("PERSON", frame)
#         if cv2.waitKey(1) & 0XFF == ord('q'):
#             break
#     cap.release()
#     cv2.destroyAllWindows()

@app.route('/person', methods=['GET'])
def get_count():
    return str(person)

@app.route('/information', methods=['POST'])
def post_information():
    global info
    data = request.json
    # info = data.get('info')
    info['fifth'] = data.get('fifth')
    info['sixth'] = data.get('sixth')
    info['seventh'] = data.get('seventh')
    info['eighth'] = data.get('eighth')
    return info

@app.route('/info', methods=['GET'])
@cross_origin() 
def get_information():
    return jsonify(info)

@app.route('/temperature', methods=['POST'])
def post_temperature():
    global temperature_humidity
    data = request.json
    temperature_humidity['temp'] = float(data.get('temp'))
    temperature_humidity['hum'] = float(data.get('hum'))
    return temperature_humidity

@app.route('/temp', methods=['GET'])
@cross_origin() 
def get_temperature():
    return jsonify(temperature_humidity)

@app.route('/floor5p', methods=['POST'])
@cross_origin()
def post_floor5():
    # data = json.loads(request.data)
    global lantai5
    data = request.json
    for i in range(len(lantai5)) :
        lantai5[i]['status'] = data[i].get('status')
        lantai5[i]['hari'] = data[i].get('hari')
        lantai5[i]['kode'] = data[i].get('kode')
        lantai5[i]['servis'] = data[i].get('servis')
    return lantai5

@app.route('/floor5g', methods=['GET'])
@cross_origin()
def get_floor5():
    global lantai5
    return jsonify(lantai5)
         
if __name__ == '__main__':
    # Thread(target=video_capture).start()
    app.run(host='0.0.0.0')