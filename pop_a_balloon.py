points = 0

def pop_balloon(color):

    if color == "red":
        return 100

    elif color == "blue":
        return 200

    elif color == "green":
        return 420

    elif color == "black":
        return -500

    else:
        return 0


for turn in range(3):

    color = input(
        "What color balloon do you want to pop? "
        "(blue/red/black/green): "
    )
    balloon_points = pop_balloon(color)
    points += balloon_points
    print("You got " + str(balloon_points) + " points!")


print("Final score:", points)
 
          