from flask import Flask, request, jsonify
from classifier import classify_ticket

app = Flask(__name__)

@app.route('/classify', methods=['POST'])
def classify():
    try:
        data = request.get_json()
        result = classify_ticket(data)
        return jsonify(result), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400


@app.route('/', methods=['GET'])
def home():
    return jsonify({
        "message": "VibeFI AI - Ticket Classification Service",
        "usage": "POST JSON to /classify endpoint"
    })

if __name__ == "__main__":
    app.run(debug=True)
