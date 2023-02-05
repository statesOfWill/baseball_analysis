import os

import flask
from flask import request, jsonify

app = flask.Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello, worldy world!"

@app.route('/api/v1/readGames', methods=['GET'])
def api_filter():
    query_parameters = request.args
    focusTeam = query_parameters.get('focus')
    opps = query_parameters.get('opponents')
    yearRange = query_parameters.get('years')
    oppsList = []
    years = []

    for year in yearRange.split(' '):
        years.append(year)

    for opp in opps.split(' '):
        oppsList.append('\"'+opp+'\"')

    return jsonify(readGames('\"'+focusTeam+'\"', oppsList, years))

def readGames(focusTeam, oppsList, years):
    return [focusTeam,oppsList,years]

app.run(host='0.0.0.0', port=8080)