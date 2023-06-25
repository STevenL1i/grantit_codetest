from flask import *

import data

# front to back end communication part
app = Flask("__name__")

@app.after_request
def cors(environ):
    environ.headers["Access-Control-Allow-Origin"] = "*"
    environ.headers["Access-Control-Allow-Method"] = "*"
    environ.headers["Access-Control-Allow-Headers"] = "Origin, X-Requested-With, Content-Type, Accept"
    return environ


@app.route("/crawldata", methods=["POST"])
def crawldata():
    req = request.get_data()
    req = json.loads(req)

    result = data.crawlbookdata()

    return jsonify(result)

@app.route("/getdata", methods=["GET"])
def getdata():
    result = data.getbookdata()

    return jsonify(result)

@app.route("/deletedata", methods=["POST"])
def deletedata():
    req = request.get_data()
    req = json.loads(req)

    result = data.deletebookdata()

    return jsonify(result)

app.run(host='0.0.0.0', port=9001)
