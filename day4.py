from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import random

x,y,z=mc.player.getTilePos()

for i in range(20):
    r=random.randrange(1,5)
    
    if r==1:
        mc.setBlocks(x,y,z,x+4,y,z,57)
        x=x+4
    elif r==2:
        mc.setBlocks(x,y,z,x-4,y,z,57)
        x=x-4
    elif r==3:
        mc.setBlocks(x,y,z,x,y,z+4,57)
        z=z+4
    elif r==4:
        mc.setBlocks(x,y,z,x,y,z-4,57)
        z=z-4
        
for i in range(10):
    x,y,z=mc.player.getTilePos()
    x=x+i
    
    for j in range(10):
        r=random.randrange(0,16)
        z=z+1
        mc.setBlock(x,y,z,35,r)
        
r=random.randrange(0,16)
while True:
    hits=mc.events.pollBlockHits()
    
    if len(hits)>0:
        hit=hits[0]
        
        block=mc.getBlockWithData(hit.pos)
        data=block.data
        
        if data==r:
            mc.postToChat('congratulation!')
            mc.setBlock(hit.pos,57)
            break
        elif data<r:
            mc.postToChat('bigger ID')
        
        elif data>r:
            mc.postToChat('smaller ID')
            
myID=mc.getPlayerEntityId('NemoNick')
mc.postToTitle(myID,'hello')
            
list2d=[[155,0,155,155,155,155,155],
        [155,0,0,0,0,0,155],
        [155,0,155,155,155,0,155],
        [155,0,0,0,0,155,155],
        [155,0,155,155,0,0,155],
        [155,0,0,0,155,0,155],
        [155,155,155,155,155,0,155]]

x,y,z=mc.player.getTilePos()
startX=x
startZ=z

for j in range(4):
    for list1d in list2d:
        for i in list1d:
            mc.setBlock(x,y,z,i)
            x=x+1
        x=startX
        z=z+1
    z=startZ
    y=y+1
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    



