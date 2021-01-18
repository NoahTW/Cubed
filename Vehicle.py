#
#
import bge
cont = bge.logic.getCurrentController()
scene = bge.logic.getCurrentScene()
own = cont.owner
def getcharrig():
	for charrig in own.children:
		if 'LadderAnim' in charrig:
			print("got " + charrig.name)
			return charrig
charrig = getcharrig()
def getheadempty():
	for headempty in bge.logic.getCurrentController().owner.children:
		if 'HeadEmpty' in headempty:
			print("V got  " + headempty.name)
			return headempty
headempty = getheadempty()
def getaimempty(headempty):
	for aimempty in headempty.children:
		if 'AimEmpty' in aimempty:
			print("got " + aimempty.name)
			return aimempty
aimempty = getaimempty(headempty)
def gethandrig(aimempty):
	for handrig in aimempty.children:
		if 'HandLadderAnim' in handrig:
			print("got " + handrig.name)
			return handrig
handrig = gethandrig(aimempty)

def getvehicleexit():
	if own['Parent'] == 'Bike1' or own['Parent'] == 'Car1':
		for vexit in own.parent.parent.children:
			if 'Exit' in vexit:
				print("got " + vexit.name)
				return vexit
Vexit = getvehicleexit()
	
	
def exitvehicle(Vexit, headempty):
		#exit and exit orientation
	vehiclerot = Vexit.parent['Rotation']
	own.removeParent()
	own.worldPosition  = Vexit.worldPosition
	own.worldOrientation = [[1.0, 0.0, 0.0], [vehiclerot*3, 1.0, 0.0], [ 0.0, 0.0, 1.0]]
	#go back to state one, and disable bike riding
	cont.activate(cont.actuators["track1"])
	own['Parent'] = ""
	headempty.state = 1
	Vexit.parent.state = 1
	#Set State to 16
	own.state = 32768

def car1(Vexit, headempty):
	cont.activate(cont.actuators["CarRiding1Anim"])
	if bge.logic.keyboard.events[bge.events.EKEY] == bge.logic.KX_INPUT_JUST_ACTIVATED:
		cont.deactivate(cont.actuators["CarRiding1Anim"])
		exitvehicle(Vexit, headempty)


def bike1(Vexit, headempty):
	cont.activate(cont.actuators["BikeRiding1Anim"])
	if bge.logic.keyboard.events[bge.events.EKEY] == bge.logic.KX_INPUT_JUST_ACTIVATED:
		exitvehicle(Vexit, headempty)

def climbladder(charrig, handrig, headempty):
	cont.activate(cont.actuators['LadderAnim1'])
	cont.activate(cont.actuators['LadderAnim2'])
	if cont.owner.sensors['WKEY'].positive:
		cont.activate(cont.actuators['LadderUp'])
		charrig['LadderAnim'] = charrig['LadderAnim'] +1
	else:
		cont.deactivate(cont.actuators['LadderUp'])
		
	if cont.owner.sensors['SKEY'].positive:
		charrig['LadderAnim'] = charrig['LadderAnim'] -1
		cont.activate(cont.actuators['LadderDown'])
	else:
		cont.deactivate(cont.actuators['LadderDown'])
	handrig['HandLadderAnim'] = charrig['LadderAnim']
	
	dist = 0
	bottomtop = None
	for item in cont.sensors["NearLadder"].hitObjectList:
		if item.getDistanceTo(own) < dist or dist == 0:
			dist = item.getDistanceTo(own)
			bottomtop = item
		def ladderexit():
			cont.deactivate(cont.actuators['LadderAnim1'])
			cont.deactivate(cont.actuators['LadderAnim2'])
			cont.activate(cont.actuators["R_Arm_0"])
			cont.activate(cont.actuators["L_Arm_0"])
			own.removeParent()
			own.worldPosition = bottomtop.children[0].worldPosition
			own.worldOrientation = bottomtop.children[0].worldOrientation

		#go back to state one, and disable Ladder
			headempty.state = 1
			own['Parent'] = ""
		#Set State to 16
			own.state = 32768
		
		if bottomtop['Ladder'] == "Bottom" and cont.owner.sensors["SKEY"].positive:
			ladderexit()
		elif bottomtop['Ladder'] == "Top" and cont.owner.sensors["WKEY"].positive:
			ladderexit()
	
		
def main():

	if own['Parent'] == 'Bike1':
		bike1(Vexit, headempty)
	if own['Parent'] == 'Car1':
		car1(Vexit, headempty)
	if own['Parent'] == 'Ladder':
		climbladder(charrig, handrig, headempty)
	 
		
main()