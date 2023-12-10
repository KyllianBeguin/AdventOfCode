# Day 1 - Trebuchet

import os

def _readInput():
    path = os.getcwd().replace("python", ".input")
    return [i.replace('\n', '') for i in open(path, 'r').readlines()]

def _getInts(text):
    return tuple(
        character 
        for character
        in text
        if character.isdigit()
    )

def _concatFirstAndLastDigit(digit_list):
    return digit_list[0] + digit_list[-1]

def partOne():
    adventInput = _readInput()
    intsLists = [
        _getInts(line)
        for line
        in adventInput
    ]
    firstAndLast = [
        int(_concatFirstAndLastDigit(intsList))
        for intsList
        in intsLists
    ]
    print("Solution to part one:", sum(firstAndLast))
    return firstAndLast

def _getFirstAndLast(text):
    First = None
    Last = None

    SpelledDigit = ['one','two','three','four','five','six','seven','eight','nine']
    mapperSpelledDigit = {
        spelled : str(pos + 1)
        for pos, spelled in enumerate(SpelledDigit)
    }
    mapperConcatSpelled = {
        spelled[:-1] + spelled2 : str(pos + 1) + str(pos2 + 1)
        for pos2, spelled2 in enumerate(mapperSpelledDigit)
        for pos, spelled in enumerate(mapperSpelledDigit)
        if spelled[-1] == spelled2[0]
    }
    mapperAllCases = mapperConcatSpelled | mapperSpelledDigit

    for posChar, character in enumerate(text):
        if character.isdigit():
            First = character
            break
        for spelled, value in mapperAllCases.items():
            if text[posChar:posChar + len(spelled)] == spelled:
                First = value[0]
                break
        if First:
            break

    for posCharReverse, character in enumerate(text[::-1]):
        posChar = len(text) - posCharReverse - 1
        if character.isdigit():
            Last = character
            break
        for spelled, value in mapperAllCases.items():
            if text[posChar:posChar + len(spelled)] == spelled:
                Last = value[len(value) - 1]
                break
        if Last:
            break

    return int(First + Last)

def partTwo():
    adventInput = _readInput()
    firstAndLast = tuple(
        _getFirstAndLast(line)
        for line
        in adventInput
    )
    print("Solution to part two:", sum(firstAndLast))
    return firstAndLast

if __name__ == "__main__":
    solutionPartOne = partOne()
    solutionPartTwo = partTwo()
