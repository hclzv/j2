from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/", methods=["GET"])
def hello():
    return jsonify({"message": "Hello from Flask on Vercel!"})

def handler(request, *args, **kwargs):
    return app(request, *args, **kwargs)
