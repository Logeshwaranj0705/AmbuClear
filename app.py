from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)

CORS(app)
@app.route('/location', methods=['POST'])
def location():
    try:
        # Force Flask to parse the incoming JSON payload
        data = request.get_json(force=True)
        print(f"Received location: {data}")  # Print the received data in the terminal
        return jsonify({"status": "success"})
    except Exception as e:
        return jsonify({"status": "failure", "error": str(e)}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
