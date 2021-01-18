import bge
if 'hairmesh' not in bge.logic.globalDict and 'playercolor' not in bge.logic.globalDict and 'haircolor' not in bge.logic.globalDict:
	bge.logic.globalDict['playercolor'] = [0.8, 0.8, 0.8, True]
	bge.logic.globalDict['haircolor'] = [0.8, 0.8, 0.8, True]
	bge.logic.globalDict['hairmesh'] = "NoHair"
def getheadempty():
	for headempty in bge.logic.getCurrentController().owner.parent.parent.children:
		if 'HeadEmpty' in headempty:
			print("init " + headempty.name)
			return headempty
headempty = getheadempty()

objects = {
# 'laser' : bge.logic.getCurrentScene().objects['Laser'],

}

def loadcolor():
	cont = bge.logic.getCurrentController()
	cont.owner.color = bge.logic.globalDict['playercolor']
	cont.owner.state = 32768
def loadhair():
	cont = bge.logic.getCurrentController()
	cont.owner.replaceMesh(bge.logic.globalDict['hairmesh'])
	cont.owner.color = bge.logic.globalDict['haircolor']
	cont.owner.state = 32768
def loadplayerlocation():
	cont = bge.logic.getCurrentController()
	scene = bge.logic.getCurrentScene()
	#cont.owner.worldPosition = bge.logic.getCurrentScene().objects['Spawn1'].worldPosition#bge.logic.globalDict['CharacterPosition']
	#if bge.logic.globalDict['inventory1'] != "":
	
	
		# If our saved inventory was not empty, add our saved inventory
	if bge.logic.globalDict['inventory1'] != "":
		inv1 = scene.objects['inventoryslot1']
		inv1item = scene.addObject(bge.logic.globalDict['inventory1'], "Player", 0)
		inv1item.setParent(inv1, 0, 1)
		if 'pickup' in inv1item:
			del inv1item['pickup']
		if 'Interact' in inv1item:
			del inv1item['Interact']
		inv1item.worldPosition = inv1.worldPosition
		inv1item.worldOrientation = inv1.worldOrientation
		cont.owner['inventory1'] = inv1item.name
	if bge.logic.globalDict['inventory2'] != "":
		inv2 = scene.objects['inventoryslot2']
		inv2item = scene.addObject(bge.logic.globalDict['inventory2'], "Player", 0)
		inv2item.setParent(inv2, 0, 1)
		if 'pickup' in inv2item:
			del inv2item['pickup']
		if 'Interact' in inv2item:
			del inv2item['Interact']
		inv2item.worldPosition = inv2.worldPosition
		inv2item.worldOrientation = inv2.worldOrientation
		cont.owner['inventory2'] = inv2item.name
	





	
	cont.owner.worldPosition.x = bge.logic.globalDict['playerposx']
	cont.owner.worldPosition.y = bge.logic.globalDict['playerposy']
	cont.owner.worldPosition.z = bge.logic.globalDict['playerposz']
	cont.activate(cont.actuators['RestoreDynamics'])
	headempty.state = 1
	bge.logic.mouse.visible = False
	cont.owner.state = 32768
	
	


def inithair():
	#if 
	cont = bge.logic.getCurrentController()
	cont.owner.replaceMesh(bge.logic.globalDict['hairmesh'])
	cont.owner.color = bge.logic.globalDict['haircolor']

def initcolor():
	cont = bge.logic.getCurrentController()
	cont.owner.color = bge.logic.globalDict['playercolor']




