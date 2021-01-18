import bge
cont = bge.logic.getCurrentController()
#own = cont.owner
#cene = bge.logic.getCurrentScene()
bge.logic.mouse.visible = True
if 'hairmesh' not in bge.logic.globalDict and 'playercolor' not in bge.logic.globalDict and 'haircolor' not in bge.logic.globalDict:
	bge.logic.globalDict['playercolor'] = [0.8, 0.8, 0.8, True]
	bge.logic.globalDict['haircolor'] = [0.8, 0.8, 0.8, True]
	bge.logic.globalDict['hairmesh'] = "NoHair"

#############  CHARACTER COLOR   #########################
def randomcolor():
      randR = bge.logic.getRandomFloat()
      randG = bge.logic.getRandomFloat()
      randB = bge.logic.getRandomFloat()
      bge.logic.globalDict['playercolor'] = [randR, randG, randB, True]
      

def maincolor():
    cont = bge.logic.getCurrentController()

    if cont.sensors['MouseRed'].positive and cont.sensors['MouseClick'].positive:
      bge.logic.globalDict['playercolor'] = [1, 0, 0, True]
    if cont.sensors['MouseGreen'].positive and cont.sensors['MouseClick'].positive:
      bge.logic.globalDict['playercolor'] = [0, 1, 0, True]
    if cont.sensors['MouseBlue'].positive and cont.sensors['MouseClick'].positive:
      bge.logic.globalDict['playercolor'] = [0, 0, 1, True]
    if cont.sensors['MouseRandomCol'].positive and cont.sensors['MouseClick'].positive:
      randomcolor()
    #print(bge.logic.globalDict)
    #own.color = bge.logic.globalDict['playercolor']

    
    
#############  CHARACTER COLOR   #########################





#############  HAIR COLOR   #########################
def randomhaircolor():
      randR = bge.logic.getRandomFloat()
      randG = bge.logic.getRandomFloat()
      randB = bge.logic.getRandomFloat()
      bge.logic.globalDict['haircolor'] = [randR, randG, randB, True]    

def haircolor():
    cont = bge.logic.getCurrentController()
    if cont.sensors['MouseBlack'].positive and cont.sensors['MouseClick'].positive:
      bge.logic.globalDict['haircolor'] = [0.035, 0.035, 0.035, True]
    if cont.sensors['MouseBrown'].positive and cont.sensors['MouseClick'].positive:
      bge.logic.globalDict['haircolor'] = [0.168, 0.024, 0.012, True]
    if cont.sensors['MouseYellow'].positive and cont.sensors['MouseClick'].positive:
      bge.logic.globalDict['haircolor'] = [1, 1, 0, True]
    if cont.sensors['MouseRandomHairCol'].positive and cont.sensors['MouseClick'].positive:
      randomhaircolor()
    #own.color = bge.logic.globalDict['haircolor']

#############  HAIR COLOR   #########################



#############   HAIR MESH     ############################

def hairmesh():
    cont = bge.logic.getCurrentController()
    if cont.sensors['Mouse.000'].positive and cont.sensors['MouseClick'].positive:
        bge.logic.globalDict['hairmesh'] = "Hair.000"
    if cont.sensors['Mouse.001'].positive and cont.sensors['MouseClick'].positive:
        bge.logic.globalDict['hairmesh'] = "Hair.001"
    if cont.sensors['Mouse.002'].positive and cont.sensors['MouseClick'].positive:
        bge.logic.globalDict['hairmesh'] = "Hair.002"
    if cont.sensors['Mouse.003'].positive and cont.sensors['MouseClick'].positive:
        bge.logic.globalDict['hairmesh'] = "Hair.003"
    if cont.sensors['Mouse.004'].positive and cont.sensors['MouseClick'].positive:
        bge.logic.globalDict['hairmesh'] = "Hair.004"
    if cont.sensors['Mouse.005'].positive and cont.sensors['MouseClick'].positive:
        bge.logic.globalDict['hairmesh'] = "Hair.005"
    if cont.sensors['Mouse.006'].positive and cont.sensors['MouseClick'].positive:
        bge.logic.globalDict['hairmesh'] = "Hair.006"
    if cont.sensors['Mouse.007'].positive and cont.sensors['MouseClick'].positive:
        bge.logic.globalDict['hairmesh'] = "Hair.007"
    if cont.sensors['Mouse.008'].positive and cont.sensors['MouseClick'].positive:
        bge.logic.globalDict['hairmesh'] = "Hair.008"
    if cont.sensors['Mouse.009'].positive and cont.sensors['MouseClick'].positive:
        bge.logic.globalDict['hairmesh'] = "Hair.009"




#############  HAIR MESH   #########################














