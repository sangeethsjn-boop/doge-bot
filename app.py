from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "DOGE Bot Running ✅"

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    print("Received signal:", data)
    return jsonify({"status": "received"})

if __name__ == "__main__":
    app.run()
