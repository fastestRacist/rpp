from flask import Flask, request, jsonify
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
import json

app = Flask(__name__)

limiter = Limiter(key_func = get_remote_address, default_limits=["100 per day"])
limiter.init_app(app)


with open("data.json", "r") as f:
    data = json.load(f)


def save_data():
    with open("data.json", "w") as f:
        json.dump(data, f)


@app.route("/set", methods=["POST"])
@limiter.limit("10 per minute")
def set_value():
    req = request.json
    data[req["key"]] = req["value"]
    save_data()
    return jsonify({"message": "сохранено"})


@app.route("/get/<key>", methods=["GET"])
def get_value(key):
    return jsonify({"value": data.get(key)})


@app.route("/delete/<key>", methods=["DELETE"])
@limiter.limit("10 per minute")
def delete_value(key):
    if key in data:
        del data[key]
        save_data()
    return jsonify({"message": "удалено"})


@app.route("/exists/<key>", methods=["GET"])
def exists(key):
    return jsonify({"exists": key in data})

if __name__ == "__main__":
    app.run(debug=True)