from hashlib import sha256
import multiprocessing
from flask import Flask, request, jsonify
from uuid import uuid4
import threading

host_name = "0.0.0.0"
port = 6069

app = Flask(__name__)             # create an app instance


@app.route("/data_d", methods=['POST'])
def data_digit_msg_receive():
    try:
        content = request.json
        print(f"[DATA] получено цифровое значение: {content['value']}")
    except:
        return "BAD DATA RESPONSE", 400
    return jsonify({"operation": "data_d", "status": True})

@app.route("/data_a", methods=['POST'])
def data_analog_msg_receive():
    try:
        content = request.json
        print(f"[DATA] получено аналоговое значение: {content['value']}")
    except:
        return "BAD DATA RESPONSE", 400
    return jsonify({"operation": "data_a", "status": True})

@app.route("/diagnostic", methods=['POST'])
def diagnostic_msg_receive():
    try:
        content = request.json
        print(f"[DIAGNOSTIC] проверка завершена со статусом: {content['status']}")
    except:
        return "BAD DIAGNOSTIC RESPONSE", 400
    return jsonify({"operation": "diagnostic", "status": True})

@app.route("/key", methods=['POST'])
def key_msg_receive():
    try:
        content = request.json
        print(f"[KEY] изменен ключ: {content['key']}")
    except:
        return "BAD KEY RESPONSE", 400
    return jsonify({"operation": "key", "status": True})

@app.route("/error", methods=['POST'])
def err_msg_receive():
    try:
        content = request.json
        print(f"[ERROR] произошла ошибка: {content['error']}")
    except:
        return "BAD ERROR RESPONSE", 400
    return jsonify({"operation": "error", "status": True})

if __name__ == "__main__":        
    app.run(port = port, host=host_name)