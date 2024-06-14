from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/data', methods=['POST'])
def receive_data():
    suhu = request.form.get('suhu')
    kelembapan = request.form.get('kelembapan')

    if suhu and kelembapan:
        response = {
            'status': 'success',
            'data': {
                'suhu': suhu,
                'kelembapan': kelembapan
            }
        }
    else:
        response = {
            'status': 'failed',
            'message': 'Invalid data'
        }
    
    return jsonify(response)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)