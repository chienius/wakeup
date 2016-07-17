#!/usr/bin/env python3
from flask import Flask, session, redirect, url_for, request, render_template
import subprocess
from urllib.request import urlopen
from urllib.error import URLError
from .config import config

WOL_COMMAND = config.WOL_COMMAND

TARGET_MAC = config.TARGET_MAC
TARGET_SERVER = config.TARGET_IP + '' + config.TARGET_PORT

LOGIN_TOKEN = config.TOKEN

app = Flask(__name__)

app.secret_key = config.SECRET

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method=='POST':
        if request.form['token'] == LOGIN_TOKEN:
            print(request.form['token'])
            session['login'] = True
            return redirect(url_for('home'))
        else:
            return redirect(url_for('login'))
    else:
        return render_template('login.html')

@app.route('/')
def home():
    if 'login' in session and session['login']:
        return render_template('home.html')
    else:
        return redirect(url_for('login'))

@app.route('/detect')
def detect():
    if 'login' in session and session['login']:
        try:
            r = urlopen('http://'+TARGET_SERVER, timeout=2)
        except Exception:
            return '0'
        else:
            if r.getcode() == 200:
                return '1'
            else:
                return '0'
    else:
        return redirect(url_for('login'))

@app.route('/wake')
def wake():
    if 'login' in session and session['login']:
        try:
            run_result = subprocess.call([WOL_COMMAND, TARGET_MAC])
        except Exception:
            return '0'
        else:
            if returncode == 0:
                return '1'
            else:
                return '0'
    else:
        return redirect(url_for('login'))

@app.route('/sleep')
def sleep():
    if 'login' in session and session['login']:
        try:
            r = urlopen('http://'+TARGET_SERVER+'/sleep?secret='+config.SECRET, timeout=2)
        except Exception:
            return '1'
        else:
            if r.getcode() == 200:
                return '1'
            else:
                return '0'
    else:
        return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session.pop('login', None)
    return redirect(url_for('login'))

def run():
    app.run(port=config.SERVER_PORT, host='0.0.0.0')
