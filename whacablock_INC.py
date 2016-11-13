# WHAC-A-BLOCK STYLE GAME ON MINECRAFT PLATFORM (inspired by the game Whac-a-Mole
# ORIGINAL CODE FROM (WWW.RASPBERRYPI.ORG)
# REWRITTEN AND EDITED AS A LEARNING PROJECT - BY BEN WOODFIELD 2/1/2016
# PROBLEM - code was initially copied exactly (with the exeption of swapping the glowing blocks to a standard gold ones because I had trouble loading the glowing ones (BLOCK ID: 14 used instead of 89) The problem displayed is 'line 33....zPos not defined' 

import mcpi.minecraft as minecraft#needed to interact with minecraft
#import mcpi.block as block#needed to refer to blocks by name rather than id
import random#used to create random numbers
import time#is used to put delays in to the code

mc = minecraft.Minecraft.create()
mc.postToChat("Minecraft Whac-A-Block")

pos = mc.player.getTilePos()
mc.setBlocks(pos.x -1, pos.y, pos.z + 3,
             pos.x + 1, pos.y + 2, pos.z + 3, 1)

mc.postToChat("Get Ready.....")
time.sleep(3)
mc.postToChat("Go!")

blocksLit = 0
points = 0
while blocksLit < 9:
    time.sleep(0.3)

    blocksLit = blocksLit + 1
    lightCreated = False
    while not lightCreated:
        xPos = pos.x + random.randint(-1,1)
        yPos = pos.y + random.randint(0,2)
        zpos = pos.z + 3

        if mc.getBlock(xPos, yPos, zPos) == 1:#when running the program, no blocks light up and a message displays 'line 33....zPos not defined'
            mc.setBlock(xPos, yPos, zPos, 14)
            lightCreated = True

            for hitBlock in mc.events.pollBlockHits():
                if mc.getBlock(hit.pos.x, hitBlock.pos.y, hitblock.pos.z) == 14:
                    mc.setBlock(hitBlock.pos.x, hitBlock.pos.y, hitBlock.pos.z, 1)
                    blocksLit = blocksLit - 1
                    points = points + 1

                    mc.postToChat("GAME OVER.....Your Points = " + str(points))

    
