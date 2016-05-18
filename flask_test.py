#! python

from flask import Flask
import os
import numpy

app = Flask(__name__)

port=int(os.getenv("PORT", 64781))

@app.route("/search")
def get_search():
    a = numpy.abs(-1.0)
    return 'Hello World'+str(a)

if __name__=='__main__':
    app.run(host='0.0.0.0',port=port)

