# Actions Dictionary
actions = {'inspect': 1, 'go': 2, 'use': 3, 'pick up': 4,}


playerInput = input("What do you want to do? ")
WasFound = False
for key in actions:
    if key in playerInput:
        WasFound = True
        print ('you ' + key)
if WasFound == False:
    print ('I DO NOT UNDERSTAND')
