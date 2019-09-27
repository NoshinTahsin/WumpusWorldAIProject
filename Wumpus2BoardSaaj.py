import sys
import os
import math
import random

# Tile Structure
class WorldCellState:
    breeze = False;
    stench = False;
    wumpus = False;
    pit    = False;
    gold   = False;
    glitter= False;
    bump=False;
    wall=False;
    safe=False;
    goldCollected=False;
    visited=False;
    #currentPosition=[]

class AgentCellState:

    agentSafe=False;
    goldCollected=False;
    visited=False;
    mayPit=False;
    mayWumpus=False;
    score=0;
    agentCurrentPosition=[]

colDimension = 10
rowDimension = 10

board = [[WorldCellState() for j in range(colDimension)] for i in range(rowDimension)]
agentBoard = [[AgentCellState() for j in range(colDimension)] for i in range(rowDimension)]


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



def main():


    #board = [[cellState() for j in range(colDimension)] for i in range(rowDimension)]
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


    #printBoard
    #initiate board for agent
    #score=0, visited=false, agentSafe=false, mayPit=false, mayWumpus=false
    #startgame 0,0
    #0,0 visited true agentsafe true

    #stage 1: get directions from current position , keep them on map with score struct ei ase, randomly choose , change agentCurrentPosition
    #put it on stack , perceive, change struct variables, map this node/cell with point,
    #check map fringe, jei cell er point shb cheye beshi oitay jawa lagbe ekhn,
        #shb point same hoile jekhane asi shekhan thke abar stage 1, loop,

        #jodi shb point same na hoy tahole jekhane asi shekhan thke pop
        # korte korte back korte thakbo ar current position check korte thakbo konta shbcheye beshi score,1 ta highest er khetre

            #jodi current position target position er sathe match kore tahole oitai current position, oikahn thke abar stage 1 loop

            #nahoy jodi current position 0,0 hoy , tokhon oikhan thke dekha lagbe j target position er (row kotocolumn koto)
                #row 4 hoile row=0 er sathe 4 plus kore 4 ghor agano lagbe for loop
                #column 3 hoile col=0 er sathe 3 ghor jog kore agano lagbe
                #oi ghore shesh mesh giye pouchailam
                #stage 1 loop


        #onekgula same highest score thakle?
            #
            #

    #
