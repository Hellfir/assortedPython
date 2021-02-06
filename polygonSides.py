def pgonSides(array):
    #initialized at 1 since we start on one side
    sidesCount = 1
    #we search for first block from left to right, so we were moving right
    lastDirection = "right"
    #we search top to bottom, so we know our first boundary is at the top
    recentBoundary = "up"
    curX = 0
    curY = 0
    done = False

    #find topmost, leftmost pixel
    curX,curY=findShape(array)
    
    #to remember when to stop
    startX = curX
    startY = curY

    while (done == False):
        #check boundaries
        #check recent boundary first
            #if still boundary, move last direction
                #if can't move last direction, turn clockwise 90 degs
            #if not, turn anticlockwise 90 degs

        if (checkBound(array,x,y,recentBoundary) == "off"):
            if (checkBound(array,x,y,lastDirection) == "on"):
                move(array,x,y,lastDirection)
            else:
                #NEEDS MORE CHECKBOUNDS
                move(array,x,y,turn(direction,"CW"))
                sidesCount += 1
                recentBoundary = direction
                lastDirection = turn(direction,"CW")
        else:
            move(array,x,y,turn(direction,"CCW"))
            sideCount += 1

        #know when sto stop
        if (curX == startX and curY == startY):
            done = True

def findShape(array):
    for (i in len(array)):
        for (j in len(array[i])):
            if (array[i][j]=="on"):
                return i,j
            else:
                continue

def getDiff(x,y,direction):
    xDiff = 0
    yDiff = 0
    if (direction=="left"):
        yDiff = -1
    elif (direction=="right"):
        yDiff = 1
    elif (direction=="up"):
        xDiff = -1
    elif (direction=="down"):
        xDiff = 1
    return x,y = x+xDiff,y+yDiff

def checkBound(array,x,y,direction):
    newX,newY = getDiff(x,y,direction)
    return array[newX][newY]

def move(array,x,y,direction)
    newX,newY = getDiff(x,y,direction)
    if (array[newX][newY]=="on"
            return newX,newY

def turnDir(direction,turn):
    dirs = ["up","right","down","left"]
    currDir = -2
    while (dirs[currDir] != direction):
        currDir+=1

    if (turn=="CW"):
        currDir+=1
    elif (turn=="CCW"):
        currDir -= 1
    else:
        print("stuff is fucked")
        quit()


