import os
from flask import Flask, request, jsonify

cnt = 0

app = Flask(__name__)

@app.route('/set', methods = ['GET','POST'])
def set():
    cnt = cnt + 1
    return jsonify({'text' : 'done'}) , 200

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0',port=int(os.environ.get('PORT', 80)))
