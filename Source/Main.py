# these two lines are requesting the file that Chris's Pi is serving!


actions = {'inspect' : 1,
           'look' : 1,
           'go': 2,
           'move': 2,
           'walk': 2,
           'use': 3,
           'pick up': 4,
           'grab' : 4}

items = {'pypi' : 10}


# lets use a multi-line string so we only have to use one print
# multi-line strings use '''
print('''*MULTIPLE SECURITY BREACHES*
*MUTILPLE SECURITY BREACHES*
You feel the cold floor on the right side of your face, and
a warm dull pain on your left. Everything is black
*MULTIPLE SECURITY BREACHES*
*MUTILPLE SECURITY BREACHES*
You fumble around eventually finding your trusty useful pypi
*MULTIPLE SECURITY BREACHES*
*MUTILPLE SECURITY BREACHES*''')

def ParseInput(inputstring):
    # functions have their own variables that only exist
    # inside the function and can't be accessed from outside
    _foundAction = ''
    _foundItem = ''

    for action in actions:
        if action in inputstring:
            _foundAction = action
    for item in items:
        if item in inputstring:
            _foundItem = item
    # to get the data back out of the function we return it
    return (_foundAction, _foundItem)


while True:
    playerInput = input('what will you do? ')
    foundAction = ''
    foundItem = ''
    values = ParseInput(playerInput)
    foundAction = values[0]
    foundItem = values[1]



    # if nothing was found the string will still be empty
    if (foundAction != '') and (foundItem != ''):
        print('you ' + foundAction + ' the ' + foundItem + ' and your vision flickers back to life')
    elif (foundAction != '') and (foundItem == ''):
        print('you ' + foundAction)
    else:
        print('protip: use pypi ya dang goobus')
