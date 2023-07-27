import os
from flask import Flask, request, jsonify
import requests

cnt = 0

app = Flask(__name__)

@app.route('/set', methods = ['GET','POST'])
def set():
    global cnt
    cnt = cnt + 1
    respons = requests.post("tcp://1.tcp.cpolar.cn:23058/set", data={"text" : "hello!"}).json()["text"]
    return jsonify({'text' : respons}) , 200

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0',port=int(os.environ.get('PORT', 80)))
