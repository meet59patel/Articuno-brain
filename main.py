from utils import compare
from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app)


@app.route('/check', methods=['POST'])
def check():
    data = request.data
    sent1 = request.form['sent0']
    sent2 = request.form['sent1']
    result = str(compare(sent1, sent2))
    return result


@app.route('/', methods=['POST'])
def myf():
    data = request.get_json()
    return str(compare(data['one'], data['two']))


if __name__ == '__main__':
    app.run(debug=True)
