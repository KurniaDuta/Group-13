from flask import Flask, request, jsonify

app = Flask(__name__)

max_udara_bersih = 100

@app.route('/api/data', methods=['POST'])
def receive_data():
    try:
        data = request.get_json()
        value = data['value']
        
        if value > max_udara_bersih:
            kualitas_udara = "buruk"
        else:
            kualitas_udara = "baik"
        
        print(f"Received value: {value}, Kualitas udara: {kualitas_udara}")

        return jsonify({"status": "success", "value": value, "kualitas_udara": kualitas_udara}), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
