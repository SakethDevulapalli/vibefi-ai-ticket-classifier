from flask import Flask, request, jsonify
from classifier import classify_ticket

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return jsonify({
        "message": "VibeFI AI - Ticket Classification Service",
        "usage": "POST JSON to /classify endpoint with {channel, severity, summary}"
    })

@app.route('/classify', methods=['POST'])
def classify():
    """
    API endpoint to classify incoming banking support tickets.
    """
    try:
        ticket = request.get_json()
        if not ticket:
            return jsonify({"error": "Invalid or empty JSON input"}), 400

        result = classify_ticket(ticket)
        return jsonify(result), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)
