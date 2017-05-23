# these two lines are requesting the file that Chris's Pi is serving!
import urllib.request
stevensNames = urllib.request.urlopen('http://2d77bf7a.ngrok.io/players').read().decode('ascii')

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

playerInput = input('In the total darkness you hesitate for a moment,\
 #but you know that you must... ')

# instead of using bools AND strings lets just use a string
# later we can check if it's empty to see if we found anything
foundAction = ''
foundItem = ''

# here we define a function, anything inside here we can use
# repeatedly by calling its name ParseInput
def ParseInput():
    # functions have their own variables that only exist
    # inside the function and can't be accessed from outside
    _foundAction = ''
    _foundItem = ''

    for action in actions:
        if action in playerInput:
            _foundAction = action
    for item in items:
        if item in playerInput:
            _foundItem = item
    # to get the data back out of the function we return it
    return (_foundAction, _foundItem)

# now we need to actually call the function we just defined
# and get the values out
values = ParseInput()
foundAction = values[0]
foundItem = values[1]

# if nothing was found the string will still be empty
if (foundAction is not '') and (foundItem is not ''):
    print('you ' + foundAction + ' the ' + foundItem)
else:
    print('protip: use pypi ya dang goobus')
