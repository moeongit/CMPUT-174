catch_limit = 7
release_limit = 3
trouts_needed = 5
# Sookie needs to keep track of the following
caught = 0
released = 0
trouts = 0
print('Fishing Expedition Starts')
condition = caught < catch_limit and trouts < trouts_needed # continue fishing condition

while condition: # While condition == True:
    catch = input('Trout y/n? ')
    if catch == 'y': # a trout was caught
        trouts = trouts + 1
        caught = caught + 1
    else:
        if released < release_limit:
            print('Release the fish')
            released = released + 1
        else:
            caught = caught + 1
    print(f'Caught : {caught}/{catch_limit}')
    print(f'Released: {released}/{release_limit}')
    print(f'Trouts : {trouts}/{trouts_needed}')
    condition = caught < catch_limit and trouts < trouts_needed # update condition

print('Fishing Expedition Ends')
if trouts == trouts_needed:
    print('Trout Cakes!')
else:
    print('Seafood Medley')