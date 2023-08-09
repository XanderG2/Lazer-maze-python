import random, math, os, time, json;import tkinter as tk

with open("Bounce.json", "r") as f:
    bounce = json.loads(f.read())

def initialise():
    global maze, laser, exitgate, bombs, root
    maze = []
    for i in range(12):
        maze.append(["|"," "," "," "," "," "," "," "," "," "," ","|"])
    maze[0] = ["-" for i in range(12)]
    maze[11] = ["-" for i in range(12)]
    maze[0][0] = "/";maze[0][11] = "\\";maze[11][0] = "\\";maze[11][11] = "/"
    laser = random.randint(1,10)
    maze[laser][0] = "L"
    exitgate = random.randint(1,10)
    maze[exitgate][11] = "e"
    bombs = [random.randint(13,144),random.randint(13,144),random.randint(13,144)]
    bombcount = 0
    while bombcount != 3:
        row = math.floor((bombs[bombcount]-1)/12)
        col = (bombs[bombcount]-1)%12
        if row in [0,11] or col in [0,11]:
            bombs[bombcount] = random.randint(13,144)
            continue
        elif maze[row][col-1] == "l" or maze[row][col+1] == "e":
            bombs[bombcount] = random.randint(13,144)
            continue
        else:
            maze[row][col] = "b"
        bombcount += 1
    root = tk.Tk()
    root.title("Laser maze")
    mazefunc()

def setuptk():
    global maze,rowentry,colentry,typeofentry,root
    rowentry = tk.Entry(root)
    rowentry.grid(column=1,row=13,columnspan=5)
    colentry = tk.Entry(root)
    colentry.grid(column=7,row=13,columnspan=5)
    typeofentry = tk.Entry(root)
    typeofentry.grid(column=12,row=13,columnspan=5)
    rowlabel = tk.Label(root,text="row: ").grid(column=0,row=13)
    collabel = tk.Label(root,text="col: ").grid(column=6,row=13)
    typeoflabel = tk.Label(root,text="type: ").grid(column=11,row=13)
    submitbutton = tk.Button(root,text="submit",command=submit).grid(column=0,row=14)
    shootbutton = tk.Button(root,text="Shoot",command=shoot).grid(column=1,row=14)
    
def mazefunc():
    global maze,root
    for r in range(len(maze)):
        for c in range(len(maze[r])):
            button_width = 25
            button_height = 25
            tk.Button(root,text=maze[r][c],padx=(button_width - 1) // 2, pady=(button_height - 1) // 2).grid(row=r,column=c)

def submit():
    global colentry,rowentry,typeofentry,root
    col = int(colentry.get())
    row = int(rowentry.get())
    typeof = typeofentry.get()
    if typeof not in ["/", "\\"]:
        errorlabel = tk.Label(root,text="Type must be / or \.").grid(row=15,col=0)
    elif row in [0,11]:
        errorlabel = tk.Label(root,text="Reflector must be in board, not on the edge").grid(row=15,col=0)
    elif col in [0,11]:
        errorlabel = tk.Label(root,text="Reflector must be in board, not on the edge").grid(row=15,col=0)
    else:
        maze[row][col] = typeof
    mazefunc()

def shoot():
    global maze,laser
    direction = "right"
    square = None
    squarenumber = (laser*12)+1
    while True:
        row = math.floor(squarenumber/12)
        col = squarenumber%12
        square = maze[row][col]
        if square in bounce.keys():
            direction = bounce[square][direction]
        elif square == "b":
            maze[row][col] = "💥"
            print("You died.")
            break
        elif square == "e":
            print("You won.")
            break
        elif square == "L":
            maze[row][col] = "💥"
            print("No worky")
            break
        
        if square in [" ","r","d","u","w"]:
            if direction in ["left","right"]:
                maze[row][col] = "="
            else:
                maze[row][col] = "¦"
            
        if direction == "right":
            squarenumber += 1
        elif direction == "left":
            squarenumber -= 1
        elif direction == "up":
            squarenumber -= 12
        elif direction == "down":
            squarenumber += 12
    mazefunc()

initialise()
setuptk()
root.mainloop()
