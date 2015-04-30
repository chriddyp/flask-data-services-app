#!flask/bin/python

import pandas as pd
from StringIO import StringIO
import datetime
import pandas_datareader.data as web

from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def index():
    return "Hello, World!"


@app.route('/data/<ticker>', methods=['GET'])
def yahoo(ticker):
    args = request.args

    start = datetime.datetime.strptime(args.get('start', '2010-01-01'), '%Y-%m-%d')
    end = datetime.datetime.strptime(args.get('end', '2015-04-30'), '%Y-%m-%d')

    f = web.DataReader(ticker, 'yahoo', start, end)
    buf = StringIO()
    f.to_csv(buf)
    response = buf.getvalue()
    # response = response.replace('\n', '<br>')

    return response


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9999, debug=True)
