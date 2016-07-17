#!/usr/bin/env python3
from flask import Flask, request
import subprocess
from .config import config

app = Flask(__name__)

@app.route('/')
def home():
    return 'It works!'

@app.route('/sleep')
def sleep():
    if request.args.get('secret') == config.SECRET:
        try:
            run_result = subprocess.run(['rundll32.exe', 'powrprof.dll,SetSuspendState', '0,1,0'])
            return 'Success'
        except Exception:
            return 'Failed', 500
    else:
        return 'Denied', 401

def run():
    app.run(port=config.TARGET_PORT, host='0.0.0.0')
