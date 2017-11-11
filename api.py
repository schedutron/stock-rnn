import pickle
import subprocess

from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from json import dumps

app = Flask(__name__)
api = Api(app)

class Predict(Resource):
    def get(self, sym):
        command = 'python2 main.py stock_symbol=%s --write' % sym
        subprocess.call(command.split())
        with open('api_log/'+sym+'.pkl', 'rb') as f:
            prediction = str(pickle.load(f))
            return jsonify(prediction)

api.add_resource(Predict, '/predict/<sym>') # Route_3

if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5002')