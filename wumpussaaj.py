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

def boundCheck(c,r):
    if(c>=0 and r>=0 and c<colDimension and r<rowDimension):
        return True

def addBreeze(c,r):
    if(boundCheck(c,r)):
        board[c][r].breeze=True

def addStench(c,r):
    if(boundCheck(c,r)):
        board[c][r].stench=True

def addGold(c,r):
    if(boundCheck(c,r)):
        board[c][r].gold=True

def addPit(c,r):
    if(boundCheck(c,r)):
        board[c][r].pit=True
        addBreeze(c,r+1)
        addBreeze(c,r-1)
        addBreeze(c+1,r)
        addBreeze(c-1,r)

def addWumpus(c,r):
    if(boundCheck(c,r)):
        board[c][r].wumpus=True
        addStench(c,r+1)
        addStench(c,r-1)
        addStench(c+1,r)
        addStench(c-1,r)

def printBoard():



    for r in range (rowDimension):
        cellInfo=""
        for c in range (colDimension):


            cellInfo+= "\t"+str(r) +", "+ str(c) +" : "

            if(r==0 and c==0):
                cellInfo+=" agent "


            if board[c][r].stench:
                cellInfo+="stench"

            elif board[c][r].wumpus:
                cellInfo+="wumpus"

            elif board[c][r].pit:
                cellInfo+="pit"

            elif board[c][r].breeze:
                cellInfo+="breeze"

            elif board[c][r].gold:
                cellInfo+="gold"

            elif board[c][r].glitter:
                cellInfo+="glitter"

            else:
                cellInfo+="empty"

        print(cellInfo)


        print("\n")




def addFeatures ( ):
        # Generate pits
        for r in range (rowDimension):
            for c in range (colDimension):
                if (c != 0 or r != 0) and random.randrange(10) < 3: #etaaaaaaki
                    addPit ( c, r )

        # Generate wumpus
        wummpusC = 0
        wumpusR = 0

        while wummpusC == 0 and wumpusR == 0:
            wummpusC = random.randrange(colDimension)
            wumpusR = random.randrange(rowDimension)

        addWumpus ( wummpusC, wumpusR );

        # Generate gold
        goldC = 0
        goldR = 0

        while goldC == 0 and goldR == 0:
            goldC = random.randrange(colDimension)
            goldR = random.randrange(rowDimension)

        addGold ( goldC, goldR )


def main():


    board = [[cellState() for j in range(colDimension)] for i in range(rowDimension)]
    #addFeatures()

    #print("Want to play in a random world or predefined world?")
    #inp=input("Enter 1 for random world, 2 for predefined world")
    #print(input)

    #if(inp==1):
        #generateRandomBoard
        #printBoard

    print("Showing board for random world")
    print("\n")
    addFeatures()
    printBoard()

    #if(inp==2):
        #generateDefinedBoard
        #printBoard


main()




