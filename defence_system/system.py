from hashlib import sha256
import multiprocessing
from flask import Flask, request, jsonify
from uuid import uuid4
import threading

host_name = "0.0.0.0"
port = 6068

app = Flask(__name__)             # create an app instance


@app.route("/alarm", methods=['POST'])
def alarm():
    try:
        content = request.json
        print(f"[ALARM] срабатывание аварийной защиты: {content['status']}")
    except:
        return "BAD RESPONSE", 400
    return jsonify({"status": True})


if __name__ == "__main__":        # on running python app.py
    #start_rest()
    app.run(port = port, host=host_name)