print("Welcome to treasure island!")
print("Your mission is to find the treasure.")

road = input("You're on a road, turn left or right? ").lower()

if road== "left":
    lake = input("You've come to a lake, there is an island in the middle, you see a boat approaching, wait or swim? ").lower()
    if lake== "wait":
        door = input("You arrived to the island, you see three doors, red, blue and yellow. Which color do you choose? ").lower()
        if door == "yellow":
            print("You found the treasure, you win!")
        else:
            print("Game Over!")
    else:
        print("Game Over!")
else:
    print("Game Over!")
