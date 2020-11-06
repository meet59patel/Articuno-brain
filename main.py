import * from utils
from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app)

@app.route('/check', methods=['POST'])
def check():
    data = request.data
    # convert data to body this is left variable
    sent1, sent2 = data[0], data[1]
    return compare(sent1, sent2)


if __name__ == '__main__':
    app.run(debug=True)