import os
from flask import Flask, request, jsonify
import requests
import json

app = Flask(__name__)

@app.route('/set', methods = ['GET','POST'])
def set():
    data_in = request.json
    headers = {'Content-Type': 'application/json'}
    response = requests.post("https://4172e3b2.r3.cpolar.cn/set", headers=headers, data = json.dumps(data_in)).json()["text"]
    return jsonify({'text' : response}) , 200

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0',port=int(os.environ.get('PORT', 80)))
