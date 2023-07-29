import os
from flask import Flask, request, jsonify
import requests
import json

app = Flask(__name__)

@app.route('/set', methods = ['POST'])
def set():
    data_in = request.json
    print("json")
    headers = {'Content-Type': 'application/json'}
    print("set")
    response = requests.post("https://primate-major-gecko.ngrok-free.app/set", headers=headers, data=json.dumps(data_in)).json()["text"]
    return jsonify({'text' : response}) , 200

@app.route('/get', methods = ['POST'])
def get():
    headers = {'Content-Type': 'application/json'}
    print("get")
    response = requests.post("https://primate-major-gecko.ngrok-free.app/get", headers=headers).json()
    return jsonify(response) , 200

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0',port=int(os.environ.get('PORT', 80)))
