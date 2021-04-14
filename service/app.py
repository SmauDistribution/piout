import flask
from flask import request
import json
import subprocess

app = flask.Flask(__name__)

def ParseIntoDictionary(v):
    res = {}
    elements = v.split('\\n')
    for el in elements:
        if(el != ''):
            pair = el.split(':')
            if(len(pair) == 2):
                res[pair[0]] = (pair[1][1:])
    return res

@app.route("/")
def status():
    with open("config.json") as f:
        conf = json.load(f)
        headers = request.headers
        if(headers['user'] == conf['user'] and headers['password'] == conf['password']):
            status = str(subprocess.Popen(["pistatus"], stdout=subprocess.PIPE ).communicate()[0])
            res = ParseIntoDictionary(status)
            return res
        else:
            return flask.Response(status=403)

    return flask.Response(status=500)