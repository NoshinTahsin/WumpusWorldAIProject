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

colDimension = 4
rowDimension = 4

board = [[cellState() for j in range(colDimension)] for i in range(rowDimension)]

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
    print("ashchiiii")
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
            wummpusC = random.randrange(colDimension)
            wumpusR = random.randrange(rowDimension)

        addWumpus ( wummpusR, wumpusc );

        # Generate gold
        goldC = 0
        goldR = 0

        while goldC == 0 and goldR == 0:
            goldC = random.randrange(colDimension)
            goldR = random.randrange(rowDimension)


        addGold ( goldR, goldC )


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
        printBoard()

    if(inp==2):
        generateDefinedBoard()
        printBoard()


main()




