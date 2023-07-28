import os
from flask import Flask, request, jsonify
import requests
import json

app = Flask(__name__)

@app.route('/set', methods = ['GET','POST'])
def set():
    data_in = request.json
    print("json")
    headers = {'Content-Type': 'application/json'}
    if request.method == "POST":
        print("post")
        response = requests.post("https://16006eb3.r3.cpolar.cn/set", headers=headers, data=json.dumps(data_in)).json()["text"]
        return jsonify({'text' : response}) , 200
    if request.method == "GET":
        return jsonify({'text' : "get_done"}) , 200
        print("get")
        response = requests.get("https://16006eb3.r3.cpolar.cn/set", headers=headers, data=json.dumps(data_in)).json()
        return jsonify(response) , 200

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0',port=int(os.environ.get('PORT', 80)))
