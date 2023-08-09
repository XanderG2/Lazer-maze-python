import random, math, os, time

def initialise():
    global maze, laser, exitgate, bombs
    maze = []
    for i in range(12):
        maze.append(["|","■","■","■","■","■","■","■","■","■","■","|"])
    maze[0] = ["-" for i in range(12)]
    maze[11] = ["-" for i in range(12)]
    maze[0][0] = "/";maze[0][11] = "\\";maze[11][0] = "\\";maze[11][11] = "/"
    laser = random.randint(1,10)
    maze[laser][0] = "l"
    exitgate = random.randint(1,10)
    maze[exitgate][11] = "e"
    bombs = [random.randint(13,144),random.randint(13,144),random.randint(13,144)]
    bombcount = 0
    while bombcount != 3:
        row = math.floor((bombs[bombcount]-1)/12)
        col = (bombs[bombcount]-1)%12
        if row in [0,11] or col in [0,11]:
            bombs[bombcount] = random.randint(13,144)
            print("looped...")
            continue
        elif maze[row][col-1] == "l" or maze[row][col+1] == "e":
            bombs[bombcount] = random.randint(13,144)
            print("looped...")
            continue
        else:
            maze[row][col] = "b"
        bombcount += 1
        print("looped...")
    os.system("cls") #this only works when you are running through command prompt
    for x in range(27):
        print()
    maze2 = "\n".join(" ".join(row) for row in maze)
    print(maze2)

def reflectors():
    global maze
    for x in range(27):
        print()
    print("\n".join(" ".join(row) for row in maze))
    row = int(input("Row: "))
    col = int(input("Col: "))
    typeof = input("Type: ")
    os.system("cls") #this only works when you are running through command prompt
    for x in range(27):
        print()
    if typeof not in ["/", "\\"]:
        print("Type must be / or \.")
    elif row in [0,11]:
        print("Reflector must be in board, not on the edge")
    elif col in [0,11]:
        print("Reflector must be in board, not on the edge")
        reflectors()
    else:
        maze[row][col] = typeof
        print("\n".join(" ".join(row) for row in maze))
        option = input("1.Shoot\n2.New reflector\n")
        if option == "1":
            shoot()
        elif option == "2":
            reflectors()
        else:
            print("Enter 1 or 2")
            reflectors()
        

def shoot():
    global maze,laser
    direction = "right"
    square = None
    squarenumber = (laser*12)+1
    while True:
        row = math.floor(squarenumber/12)
        col = squarenumber%12
        square = maze[row][col]

        if square == "/":
            if direction == "right":
                direction = "up"
            elif direction == "up":
                direction = "right"
            elif direction == "down":
                direction = "left"
            elif direction == "left":
                direction = "down"
        elif square == "\\":
            if direction == "left":
                direction = "up"
            elif direction == "down":
                direction = "right"
            elif direction == "up":
                direction = "left"
            elif direction == "right":
                direction = "down"
        elif square in ["-","|"]:
            if direction == "down":
                direction = "up"
            elif direction == "left":
                direction = "right"
            elif direction == "right":
                direction = "left"
            elif direction == "up":
                direction = "down"
        elif square == "b":
            maze[row][col] = "💥"
            print("You died.")
            print("\n".join(" ".join(row) for row in maze))
            break
        elif square == "e":
            print("You won.")
            print("\n".join(" ".join(row) for row in maze))
            break
        elif square == "l":
            maze[row][col] = "💥"
            print("No worky")
            print("\n".join(" ".join(row) for row in maze))
            break
        
        if square in ["■","r","d","u","w"]:
            if direction in ["left","right"]:
                maze[row][col] = "="
            else:
                maze[row][col] = "¦"
            #print("\n".join(" ".join(row) for row in maze))
            
        if direction == "right":
            squarenumber += 1
        elif direction == "left":
            squarenumber -= 1
        elif direction == "up":
            squarenumber -= 12
        elif direction == "down":
            squarenumber += 12

initialise()
reflectors()
