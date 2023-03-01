import unittest
import os
import matplotlib.pyplot as plt

from src.analyze_baseball import manyOpponentSeasonResult

class TestApi(unittest.TestCase):

    def test_baseball(self):
        results = self.basbeball()
        for seasons in results:
            
            for season in seasons:
                print(season["year"])
                data = []
                for oppRecord in season["season_result"]:
                    print(oppRecord)
            
        self.assertEqual('foo'.upper(), 'FOO')

    def readGames(self, teamOF, opps, years):
        os.chdir('./src/static')
        inputs = []
        for file_path in os.listdir():
            with open(file_path, 'r') as f:
                games = f.read()
                l = len(file_path)
                year = file_path[l-8:l-4]
                yearRange = range(int(years[0]), int(years[1]), 1) 
                count = yearRange.count(int(year))
                if (count > 0):
                    inputs.append([  games, {"year" : year, "focus_team" : teamOF, "oppNames" : opps} ])
        os.chdir('../..')
        return inputs

    def basbeball(self):
        focusTeam = "ARI"
        opps = "ANA ATL BAL BOS CHA CHN CIN CLE COL DET FLO HOU KCA LAD MIL MON MTL MYN NYA NYN OAK PHI PIT SEA SDN SFN SLN STL TBA TEX TOR"
        yearRange = "1998 2020"
        oppsList = []
        years = []
        results=[]
    
        for year in yearRange.split(' '):
            years.append(year)

        for opp in opps.split(' '):
            oppsList.append('\"'+opp+'\"')

        basbeball_inputs = self.readGames('\"'+focusTeam+'\"', oppsList, years)
        oppResults = []
        for inputs in basbeball_inputs:
            oppResults.append({"year": inputs[1]["year"], "season_result": manyOpponentSeasonResult(inputs[0], inputs[1])})
        results.append(oppResults)
        return results

if __name__ == '__main__':
    unittest.main()