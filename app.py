import os

import flask
from flask import request, jsonify

from analyze_baseball import calcNTeamSeasonResult 
from model import Input

app = flask.Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello, worldy world!"

@app.route('/api/v1/readGames', methods=['GET'])
def analyzeBaseball():
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

# BASEBALL ANALYSIS - begin
def readGames(teamOF, opps, years):
    os.chdir('static')
    seasons = []
    for file in os.listdir():
        file_path = file
        l = len(file_path)
        year = file_path[l-8:l-4]
        yearRange = range(int(years[0]), int(years[1]), 1) 
        count = yearRange.count(int(year))
        if (count > 0):
            seasonResult = calcNTeamSeasonResult(file_path, Input(year, teamOF, opps))
            seasons.append(seasonResult)
    os.chdir('..')
    return seasons
# BASEBALL ANALYSIS - end
app.run(host='0.0.0.0', port=8080)