import os
from requests import get
from flask import Flask
from flask_cors import CORS
key = os.environ.get('APIKEY')

url = f'https://www.googleapis.com/youtube/v3/channels?part=statistics&id=UCANI94YmcIGmabIDPx5oHYg&fields=items/statistics/subscriberCount&key={key}'

res = ''


def consultarApi():
    req = get(url)
    res = req.json()
    return res


app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})


@app.route('/')
def index():
    return consultarApi()


app.run(debug=True)
