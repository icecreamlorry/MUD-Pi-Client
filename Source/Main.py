actions = {'inspect' : 1,
           'look' : 1,
           'go': 2, 
           'move': 2,
           'walk': 2,
           'use': 3, 
           'pick up': 4,
           'grab' : 4}    

items = {'pypi' : 10}

print ('*MULTIPLE SECURITY BREACHES*')
print ('*MUTILPLE SECURITY BREACHES*')
print ('you feel the cold floor on the right side of your face, and a warm dull pain on your left. everything is black')
print ('*MULTIPLE SECURITY BREACHES*')
print ('*MUTILPLE SECURITY BREACHES*')
print ('you fumble around eventually finding your trusty useful pypi')
print ('*MULTIPLE SECURITY BREACHES*')
print ('*MUTILPLE SECURITY BREACHES*')

#BROKEN

playerInput = input("in the total darkness you hesitate for a moment, but you know that you must... ")
actionFound = False
itemFound = False
foundAction = ""
foundItem = ""
for action in actions:
    if action in playerInput:
        actionFound = True
        foundAction = action
for item in items:
    if item in playerInput:
        itemFound = True
        foundItem = item
if (actionFound == True) and (itemFound == True):
    print ('you ' + foundAction + ' the ' + foundItem)
else:
    print ('protip: use pypi ya dang goobus')
#BROKEN

