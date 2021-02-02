from mcpi.minecraft import Minecraft
mc = Minecraft.create()
x,y,z=mc.player.getTilePos()

x,y,z=mc.player.getTilePos()
mc.setBlocks(x,y,z,x+4,y+4,z+4,35)
mc.setBlocks(x+1,y+1,z+1,x+3,y+3,z+3,0)

x,y,z=mc.player.getTilePos()
a=int(input('想放什麼方塊'))
mc.setBlock(x,y,z,a)

name=input('enter your name:')
message=input('enter your message:')
mc.postToChat('<'+ name +'>' +message)

x,y,z=mc.player.getTilePos()
mc.setSign(x,y,z,63,0,'Hi','Are you a pig ?')

while True:
    x,y,z=mc.player.getTilePos()
    a=mc.getBlockWithData(x,y-1,z)
    if a.data==15:
        mc.postToChat('死路')
        
    if a.data==11:
        mc.postToChat('右轉')
        
while True:
    hits=mc.events.pollBlockHits()
    
    if len(hits) > 0:
        hit=hits[0]
        x,y,z=hit.pos.x,hit.pos.y,hit.pos.z
        block=mc.getBlock(x,y,z)
        
        if block==1:
            mc.setBlock(x,y,z,57)
            
x,y,z=mc.player.getTilePos()
mc.spawnEntity(x,y,z,93)
        











