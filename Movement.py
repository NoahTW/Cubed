import bge
cont = bge.logic.getCurrentController()
scene = bge.logic.getCurrentScene()
own = cont.owner
w = cont.owner.sensors["WKEY"]
s = cont.owner.sensors["SKEY"]
a = cont.owner.sensors["AKEY"]
d = cont.owner.sensors["DKEY"]
shift = cont.owner.sensors["SHIFTKEY"]
spacebar = cont.owner.sensors["SPACEBAR"]

slowwalk = cont.actuators["WalkAnim"]
fastwalk = cont.actuators["FastWalkAnim"]
Rwalk = cont.actuators["RightWalkAnim"]
Lwalk = cont.actuators["LeftWalkAnim"]
idle = cont.actuators["IdleAnim"]


#print(cont.owner.sensors)

def walk():
    if w.positive and not shift.positive and not s.positive:
        own.applyMovement([0.0, -own['walkspeed'], 0.0], True)
        cont.deactivate(fastwalk)
        cont.deactivate(Lwalk)
        cont.deactivate(Rwalk)
        cont.activate(slowwalk)
    elif w.positive and shift.positive and not s.positive:
        own.applyMovement([0.0, -own['fastwalkspeed'], 0.0], True)
        cont.deactivate(slowwalk)
        cont.deactivate(Lwalk)
        cont.deactivate(Rwalk)
        cont.activate(fastwalk)
    elif s.positive and not w.positive:
        own.applyMovement([0.0, own['walkspeed'], 0.0], True)
        cont.deactivate(fastwalk)
        cont.deactivate(Lwalk)
        cont.deactivate(Rwalk)
        cont.activate(slowwalk)
    elif a.positive and not d.positive:
        own.applyMovement([own['walkspeed'], 0.0, 0.0], True)
        cont.activate(Lwalk)
    elif d.positive and not a.positive:
        own.applyMovement([-own['walkspeed'], 0.0, 0.0], True)
        cont.activate(Rwalk)
    else:
        cont.deactivate(Lwalk)
        cont.deactivate(Rwalk)
    if not w.positive:
        cont.deactivate(fastwalk)
        cont.deactivate(slowwalk)
  #  if
	#	own.applyMovement([0.0, -own['jumpheight'], 0.0], True)
    
# if not
#     own.worldLinearVelocity*=.9
#     own.applyForce((0,0,(own.mass*9.8)),0)    
walk()

####  Create a track-to setup like the bike has.
# player tracks to *Direction* only when actually walking