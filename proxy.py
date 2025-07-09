from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route("/proxy/outages")
def proxy_outages():
    try:
        res = requests.get("https://api.poweroutage.us/utility/990/map.json", timeout=10)
        res.raise_for_status()
        return jsonify(res.json())
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
