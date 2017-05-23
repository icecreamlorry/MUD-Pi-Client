#import urllib.request

def sendActionToServer(action, item):
    print('~>sending action ' + str(action) + ' item ' + str(item))
    return

def getPositionFromServer():
    return 1

def getActionsFromServer():
    return {'inspect' : 1,
            'look' : 1,
            'go': 2,
            'move': 2,
            'walk': 2,
            'use': 3,
            'pick up': 4,
            'grab' : 4}

def getItemsFromServer():
    return {'pypi' : 10,
            'north' : 11,
            'south' : 12,
            'east' : 13,
            'west' : 14}

def ParseInput(inputstring, actions, items):
    _foundAction = ''
    _foundItem = ''

    for action in actions:
        if action in inputstring:
            _foundAction = action
    for item in items:
        if item in inputstring:
            _foundItem = item
    return(_foundAction, _foundItem)

while True:
    currentPosition = getPositionFromServer()
    currentActions = getActionsFromServer()
    currentItems = getItemsFromServer()
    print('you are in room ' + str(currentPosition))
    playerInput = input('what do you want to do? ')

    values = ParseInput(playerInput, currentActions, currentItems)
    foundAction = values[0]
    foundItem = values[1]
    if(foundAction != '') and(foundItem != ''):
        sendActionToServer(currentActions[foundAction], currentItems[foundItem])
    elif(foundAction != '') and(foundItem == ''):
        sendActionToServer(currentActions[foundAction], 0)
    else:
        print('no comprende')
