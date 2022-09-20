catch_limit = 7
release_limit = 3
trouts_needed = 5
caught = 0
released = 0
trouts = 0
print("Fishing Expedition Starts.")
condition = caught < catch_limit and trouts < trouts_needed and released < release_limit

while condition:
    catch = input("Did you catch a trout? y/n ")
    if catch == "y":
        trouts += 1
        caught += 1
    else:
        if released < release_limit:
            print("Release The Fish.")
            released += 1
    print(f"Caught: {caught}/{catch_limit}")
    print(f"Released: {released}/{release_limit}")
    print(f"Trouts: {trouts}/{trouts_needed}")
    condition = caught < catch_limit and trouts < trouts_needed and released < release_limit
print("Fishing Expedition Ends.")
if trouts == trouts_needed:
    print("Trout Cakes!")
else:
    print("No Trout Cakes.")