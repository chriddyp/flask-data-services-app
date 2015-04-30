#!flask/bin/python

import pandas as pd
from StringIO import StringIO
import datetime
import pandas_datareader.data as web

start = datetime.datetime(2010, 1, 1)
end = datetime.datetime(2013, 1, 27)

from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return "Hello, World!"


@app.route('/data/<ticker>')
def yahoo(ticker):
    try:
        f = web.DataReader(ticker, 'yahoo', start, end)
        buf = StringIO()
        f.to_csv(buf)
        response = buf.getvalue()
        response = response.replace('\n', '<br>')
    except:
        print ticker, 'not available'
        response = 'not available'

    return response


if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=9999)
