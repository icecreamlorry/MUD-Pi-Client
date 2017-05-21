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
playerInput = input ("in the total darkness you hesitate for a moment, but you know that you must... ")
WasFound = False
for key in actions, items:
    if key in playerInput:
        WasFound = True
    print ('you ' + key  + key in items)
if WasFound == False:
    print ('protip: use pypi you idiot')
#BROKEN
