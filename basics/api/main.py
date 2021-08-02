from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/d")
def hello():
    return "Hello guys"


@app.route("/", methods=["GET"])
def get_person():
    return jsonify({"name": "Andres", "age": 25})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=81, debug=True)
