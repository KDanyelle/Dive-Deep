#Task 1

place = input("Choose a place: forest or carve?")

if place == "forest":
    action = input("climb a tree or cross a river?")
if action == "clinmb a tree":
    print("You found a bird's nest!")
elif action == "cross a river":
    print("You found a boat!")
else: 
    print("Invalid action!")
elif place == "cave":
print("You find a hidden treasure!")
else:
print("Invald place")

#Task 2

place = input("cave")

if place == "cave":
    action = input("light a torch?") or ("proceed in the dark")
    print("light a torch")

#Task 3

place = input("cave")

action = input("light a torch")
pass
action = input("proceed in the dark")
pass



