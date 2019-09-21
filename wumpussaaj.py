#choose option random world or pre-defined world
#generateRandomBoard()  or generateDefinedBoard()
#
import sys
import os
import math
import random

# Tile Structure
class cellState:
    breeze = False;
    stench = False;
    wumpus = False;
    pit    = False;
    gold   = False;
    glitter= False;
    safe=False;
    pending="";
    goldCollected=False;

colDimension = 10
rowDimension = 10

board = [[cellState() for j in range(colDimension)] for i in range(rowDimension)]

#branchList={ 0: [1,10], 1: [0,2,11], 3: [1,7,8], 4: [1,9,10], 5:[2,9,11],
#				6: [2,7,12]}

def boundCheck(r,c):
    if(c>=0 and r>=0 and c<colDimension and r<rowDimension):
        return True

def addBreeze(r,c):
    if(boundCheck(r,c)):
        board[r][c].breeze=True

def addStench(r,c):
    if(boundCheck(r,c)):
        board[r][c].stench=True

def addGold(r,c):
    #print("ashchiiii")
    if(boundCheck(r,c)):
        board[r][c].gold=True
        board[r][c].glitter=True
        #print("*************"+ str(c)+ "     "+str(r))

def addPit(r,c):
    if(boundCheck(r,c)):
        board[r][c].pit=True
        addBreeze(r+1,c)
        addBreeze(r-1,c)
        addBreeze(r,c+1)
        addBreeze(r,c-1)

def addWumpus(r,c):
    if(boundCheck(r,c)):
        board[r][c].wumpus=True
        addStench(r+1,c)
        addStench(r-1,c)
        addStench(r,c+1)
        addStench(r,c-1)

def printBoard():



    for r in range (rowDimension):
        cellInfo=""
        for c in range (colDimension):


            cellInfo+= "\t"+str(r) +", "+ str(c) +" : "

            if(r==0 and c==0):
                cellInfo+=" agent "


            if board[r][c].stench:
                cellInfo+=" stench"

            if board[r][c].wumpus:
                cellInfo+=" wumpus"

            if board[r][c].pit:
                cellInfo+=" pit"

            if board[r][c].breeze:
                cellInfo+=" breeze"

            if board[r][c].gold:
                cellInfo+=" gold"

            if board[r][c].glitter:
                cellInfo+=" glitter"

            #else:
            #cellInfo+="empty"

        print(cellInfo)


        print("\n")



def printBoardForAgent():

    print("\n Showing board from agent's perspective")

    for r in range (rowDimension):
        cellInfo=""
        for c in range (colDimension):


            cellInfo+= "\t"+str(r) +", "+ str(c) +" : "

            if(r==0 and c==0):
                cellInfo+=" agent "


            if board[r][c].stench:
                cellInfo+=" stench"

            if board[r][c].breeze:
                cellInfo+=" breeze"

            if board[r][c].glitter:
                cellInfo+=" glitter"

            #else:
            #cellInfo+="empty"

        print(cellInfo)


        print("\n")




def generateDefinedBoard():
    pitList=[[0,2], [0,3], [1,0], [3,0]]
    wumpusList=[3,2]
    goldList=[3,2]

    for p in range (len(pitList)):
        pitRow=pitList[p][0]
        pitCol=pitList[p][1]
        addPit(pitRow, pitCol)

    wumpusRow=wumpusList[0]
    wumpusCol=wumpusList[1]
    addWumpus(wumpusRow, wumpusCol)

    goldRow=goldList[0]
    goldCol=goldList[1]
    addGold(goldRow, goldCol)




def addFeaturesRandomly ( ):
        # Generate pits
        for r in range (rowDimension):
            for c in range (colDimension):
                if (c != 0 or r != 0) and random.randrange(10) < 3: #etaaaaaaki
                    addPit ( r, c )

        # Generate wumpus
        wummpusC = 0
        wumpusR = 0

        while wummpusC == 0 and wumpusR == 0:
            wumpusC = random.randrange(colDimension)
            wumpusR = random.randrange(rowDimension)

        addWumpus ( wumpusR, wumpusC );

        # Generate gold
        goldC = 0
        goldR = 0

        while goldC == 0 and goldR == 0:
            goldC = random.randrange(colDimension)
            goldR = random.randrange(rowDimension)


        addGold ( goldR, goldC )


def checkStench(r,c):
    if board[r][c].stench:
        if r==0 and c==0:
            board[r][c+1].pending+=" wumpus"
            board[r+1][c].pending+=" wumpus"
        elif r==0 and c==9:
            board[r][c-1].pending+=" wumpus"
            board[r+1][c].pending+=" wumpus"
        elif r==9 and c==0:
            board[r][c+1].pending+=" wumpus"
            board[r-1][c].pending+=" wumpus"
        elif r==9 and c==9:
            board[r-1][c].pending+=" wumpus"
            board[r][c-1].pending+=" wumpus"
        elif r==0:
            board[r][c+1].pending+=" wumpus"
            board[r][c-1].pending+=" wumpus"
            board[r+1][c].pending+=" wumpus"
        elif r==9:
            board[r][c+1].pending+=" wumpus"
            board[r][c-1].pending+=" wumpus"
            board[r-1][c].pending+=" wumpus"
        else:
            board[r][c+1].pending+=" wumpus"
            board[r][c-1].pending+=" wumpus"
            board[r+1][c].pending+=" wumpus"
            board[r-1][c].pending+=" wumpus"

def checkWumpus(r,c):
    if board[r][c].wumpus==True:
        print("Wumpus Eats You! You lose! Game Over!!!")
        return True

def checkPit(r,c):
    if board[r][c].pit==True:
        print("You fell into a pit")
        return True

def checkBreeze(r,c):
    if board[r][c].breeze:
        if r==0 and c==0:
            board[r][c+1].pending+=" pit"
            board[r+1][c].pending+=" pit"
        elif r==0 and c==9:
            board[r][c-1].pending+=" pit"
            board[r+1][c].pending+=" pit"
        elif r==9 and c==0:
            board[r][c+1].pending+=" pit"
            board[r-1][c].pending+=" pit"
        elif r==9 and c==9:
            board[r-1][c].pending+=" pit"
            board[r][c-1].pending+=" pit"
        elif r==0:
            board[r][c+1].pending+=" pit"
            board[r][c-1].pending+=" pit"
            board[r+1][c].pending+=" pit"
        elif r==9:
            board[r][c+1].pending+=" pit"
            board[r][c-1].pending+=" pit"
            board[r-1][c].pending+=" pit"
        else:
            board[r][c+1].pending+=" pit"
            board[r][c-1].pending+=" pit"
            board[r+1][c].pending+=" pit"
            board[r-1][c].pending+=" pit"

def checkGlitter(r,c):
    if board[r][c].glitter==True:
        board[r][c].goldCollected=True
        print("Gold collected! Game won!")

threatInfo=""

def checkThreat(r,c):
    checkStench(r,c)
    w=checkWumpus(r,c)
    p=checkPit(r,c)
    checkBreeze(r,c)
    checkGlitter(r,c)

    if w==False and p==False:
        board[r][c].safe=True

def getAdjCellList(r,c):
    listAdj=[]
    if r==0 and c==0:
        listAdj.append([r,c+1])
        listAdj.append([r+1,c])

    elif r==0 and c==9:
        listAdj.append([r,c-1])
        listAdj.append([r+1,c])

    elif r==9 and c==0:
        listAdj.append([r,c+1])
        listAdj.append([r-1,c])

    elif r==9 and c==9:
        listAdj.append([r-1,c])
        listAdj.append([r,c-1])

    elif r==0:
        listAdj.append([r,c+1])
        listAdj.append([r,c-1])
        listAdj.append([r+1,c])

    elif r==9:
        listAdj.append([r,c+1])
        listAdj.append([r,c-1])
        listAdj.append([r-1,c])

    else:
        listAdj.append([r,c+1])
        listAdj.append([r,c-1])
        listAdj.append([r-1,c])
        listAdj.append([r+1,c])

    return listAdj


def enterCell(r,c):
    print("Agent is in cell: "+str(r)+" , "+str(c))
    checkThreat(r,c)

    while 1:
        print("You are in cell "+str(r)+" , "+str(c))
        print("You can go to cells ")
        adjacentCellList=getAdjCellList(r,c)
        print(adjacentCellList)


        #jei cell gulay jawa jay jabe bfs maybe
        #ager cell stack e rakhbe
        #shb cell er state dekhay dibe
        #print korabe thought process + set korbe value state

        #scoring bakiiiiiiiiiiiiii
        #






def startGame():
    print("Game started")

    enterCell(0,0)



def main():


    board = [[cellState() for j in range(colDimension)] for i in range(rowDimension)]
    #addFeatures()

    print("Want to play in a random world or predefined world?")
    inp=input("Enter 1 for random world, 2 for predefined world")
    print(inp)

    inp=int(inp)

    if inp==1:
        print("Showing board for random world")
        print("\n")
        addFeaturesRandomly()

    if(inp==2):
        generateDefinedBoard()
        print("Showing board for user defined world")

    printBoard()
    printBoardForAgent()

    startGame()


main()

#world generate korlo
#adjacent gula list of list e dibo--- list korar dorkar nai--bfs chalabo
#dekhbo kon cell thke koi koi jawa jay
#safe hoile safe mark korbo
#breeze/stench paile adjacent 4 ta pending mark korbo, pending er value dibo
#stack e rakhbo
#point add korbo
#koi jabo 3 dik block thkale decide korbo

##threat onnovabe fela jay ki vaba lagbe, unique kisu but random e


