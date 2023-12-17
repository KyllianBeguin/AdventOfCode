# Day 2 - Cube Conundrum 

import os
import re

def _readInput():
    path = os.getcwd().replace("python", ".input")
    return [i.replace('\n', '') for i in open(path, 'r').readlines()]

def _parseColors(line):
    """Get values and returns a list"""
    parsed = {
        "red" : re.findall(r"\d+ red", line)
        , "blue" : re.findall(r"\d+ blue", line)
        , "green" : re.findall(r"\d+ green", line)
    }
    return parsed

def _getMaximumValues(colors): 
    # Extract values and sort the list
    # print("\n", colors)
    for _color in colors.keys():
        colors[_color].sort(key = lambda x: int(x.replace(" " + _color, "")), reverse = True)
        colors[_color] = int(colors[_color][0].replace(" " + _color, ""))
    # print(colors)
    return colors

def _evaluateGame(colorsMax, gameID):
    if (colorsMax["red"] <= 12) and (colorsMax["green"] <= 13) and (colorsMax["blue"] <= 14):
        return gameID
    else:
        return 0
    
def partOne():
    adventInputs = _readInput()
    inputColors = [_parseColors(line) for line in adventInputs]
    maxValues = [_getMaximumValues(colors) for colors in inputColors]
    _ids = [_evaluateGame(colorsMax, _id+1) for _id, colorsMax in enumerate(maxValues)]
    solution = sum(_ids)
    print(solution)
    return solution

def _powerColors(colorsMax):
    return colorsMax["red"] * colorsMax["green"] * colorsMax["blue"]

def partTwo():
    adventInputs = _readInput()
    inputColors = [_parseColors(line) for line in adventInputs]
    maxValues = [_getMaximumValues(colors) for colors in inputColors]
    powersValues = [_powerColors(colorsMax) for colorsMax in maxValues]
    solution = sum(powersValues)
    print(solution)
    return solution
 
if __name__ == "__main__":
    solutionPartOne = partOne()
    solutionPartTwo = partTwo()
