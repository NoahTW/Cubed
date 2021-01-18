#Learn from men with hair on their chest. CGMasters.net
import bge


cont = bge.logic.getCurrentController()
scene = bge.logic.getCurrentScene()
own = cont.owner
name = bge.logic.globalDict['charactername']
keyboard = bge.logic.keyboard
JUST_ACTIVATED = bge.logic.KX_INPUT_JUST_ACTIVATED
inv1 = scene.objects['inventoryslot1']
inv2 = scene.objects['inventoryslot2']
Rhand = scene.objects['R_hand']
boxxytalk = {
 0 : "Boxxy",
 1 : "Hi there %s." % (name) + "\n" + "My name is Boxxy!",
 2 : "I can't talk now." + "\n" + "I have important Box things to do!"
}

def getheadempty():
	for headempty in bge.logic.getCurrentController().owner.children:
		if 'HeadEmpty' in headempty:
			print("got " + headempty.name)
			return headempty
headempty = getheadempty()
def getEtext(headempty):
	for Etext in headempty.children:
		if 'Etext' in Etext:
			return Etext
Etext = getEtext(headempty)

def getEitem():
	dist = 0
	for item in cont.sensors["NearE"].hitObjectList:
		if item.getDistanceTo(own) < dist or dist == 0:
			dist = item.getDistanceTo(own)
			return item

########Picking up an object from the ground####
def pickup(Eitem):
	pickupobj = Eitem					#remove the pickup property so the game doesnt try to pick up items already in his inventory
	if 'Interact' in pickupobj:
		del pickupobj['Interact']
				#if the object goes to slot 1.. 
	if pickupobj['inventoryslot'] == 1:
    # if our inventory slot isnt blank, and our hand is empty.
		if own['inventory1'] != "" and own['inhand'] != 1:
			#drop the old item, remove its parent, and assign it a pickup value
			droppingitem = inv1.children[0]
			droppingitem.worldPosition = scene.objects['Aim_Empty'].worldPosition
			droppingitem.worldOrientation = scene.objects['Aim_Empty'].worldOrientation
			droppingitem.removeParent()
			droppingitem['Interact'] = "Pick up"
				#assign the new item to the inventory slot
				# But if our hand IS holding Inventory item 1.....
		elif own['inventory1'] != "" and own['inhand'] == 1:
			#drop the old item FROM THE HAND, remove its parent, and assign it a pickup value
			droppingitem = Rhand.children[0]
			droppingitem.worldPosition = scene.objects['Aim_Empty'].worldPosition
			droppingitem.worldOrientation = scene.objects['Aim_Empty'].worldOrientation
			droppingitem.removeParent()
			droppingitem['Interact'] = "Pick up"	
					
				#now that our inventory/hand slot is empty, we can assign it to directly the inventory slot.
		if own['inhand'] != 1:
			pickupobj.setParent(inv1, 0, 1)
			pickupobj.worldPosition = inv1.worldPosition
			pickupobj.worldOrientation = inv1.worldOrientation
			own['inventory1'] = pickupobj.name
					#or, we can assign it to the hand, if that inventory slot is active
		elif own['inhand'] == 1:
			pickupobj.setParent(Rhand, 0, 1)
			pickupobj.worldPosition = Rhand.worldPosition
			pickupobj.worldOrientation = Rhand.worldOrientation
			own['inventory1'] = pickupobj.name
			own['handitem'] = own['inventory1']
			cont.activate(cont.actuators["R_Arm_1"])
				
	## everything the same as before, but for inventory slot 2
	elif pickupobj['inventoryslot'] == 2:
		if own['inventory2'] != "" and own['inhand'] != 2:
		    droppingitem = inv2.children[0]
		    droppingitem.worldPosition = scene.objects['Aim_Empty'].worldPosition
		    droppingitem.worldOrientation = scene.objects['Aim_Empty'].worldOrientation
		    droppingitem.removeParent()
		    droppingitem['Interact'] = "Pick up"
		elif own['inventory2'] != "" and own['inhand'] == 2:
		    droppingitem = Rhand.children[0]
		    droppingitem.worldPosition = scene.objects['Aim_Empty'].worldPosition
		    droppingitem.worldOrientation = scene.objects['Aim_Empty'].worldOrientation
		    droppingitem.removeParent()
		    droppingitem['Interact'] = "Pick up"
		if own['inhand'] != 2:
		    pickupobj.setParent(inv2, 0, 1)
		    pickupobj.worldPosition = inv2.worldPosition
		    pickupobj.worldOrientation = inv2.worldOrientation
		    own['inventory2'] = pickupobj.name
		elif own['inhand'] == 2:
		    pickupobj.setParent(Rhand, 0, 1)
		    pickupobj.worldPosition = Rhand.worldPosition
		    pickupobj.worldOrientation = Rhand.worldOrientation
		    own['inventory2'] = pickupobj.name
		    own['handitem'] = own['inventory2']
		    cont.activate(cont.actuators["R_Arm_1"])
		
	print("ran pickup()")	#### End of picking up an inventory object##
def unequipitem():
	if own['inhand'] != "":
		if own['inhand'] == 1 and own['handitem'] != "":
		    unequippingitem = Rhand.children[0]
		    unequippingitem.setParent(inv1, 0, 1)
		    unequippingitem.worldPosition = inv1.worldPosition
		    unequippingitem.worldOrientation = inv1.worldOrientation
		    own['handitem'] = ""
		    #put in invslot 2
		if own['inhand'] == 2 and own['handitem'] != "":
		    unequippingitem = Rhand.children[0]
		    unequippingitem.setParent(inv2, 0, 1)
		    unequippingitem.worldPosition = inv2.worldPosition
		    unequippingitem.worldOrientation = inv2.worldOrientation
		    own['handitem'] = ""

def inhand():
	#basic scrolling up/down to equip items.
	handslot = own['inhand']
	if cont.sensors["Mouseup"].positive:
		if handslot != 2:
		    handslot = handslot +1
		elif handslot == 2:
		    handslot = 0	
	elif cont.sensors["Mousedown"].positive:
		if handslot != 0:
		    handslot = handslot -1
		elif handslot == 0:
		    handslot = 2
		### if the active hand changes an item, put the current item into inv slot 1 or 2

	# end of scrolling#
	if handslot != own['inhand']:
		unequipitem()
		    	
		#now that the hand is empty, we can fill it with the item from the inventory slot.
		#to start with, if the new slot is 0 (empty), put nothing in it and put down our arm
	if handslot == 0 and own['inhand'] != 0 and own['handitem'] == "":
		    cont.activate(cont.actuators["R_Arm_0"]) #putting down our arm##
		    own['inhand'] = 0   

# if the new item going into the hand is from inventory slot one, take inv1's child, and put in our hand slot
	elif handslot == 1 and own['inhand'] != 1 and own['inventory1'] != "" and own['handitem'] == "":
		    equippingitem = inv1.children[0]
		    equippingitem.setParent(Rhand, 0, 1)
		    equippingitem.worldPosition = Rhand.worldPosition
		    equippingitem.worldOrientation = Rhand.worldOrientation
		    cont.activate(cont.actuators["R_Arm_1"])
		    own['handitem'] = own['inventory1']
		    own['inhand'] = 1
		#however, if there is nothing in inv1, and our active hand is 1,
		#simply put down our arm, and put nothing into the hand
	elif handslot == 1 and own['inhand'] != 1 and own['inventory1'] == "" and own['handitem'] == "":
		    own['handitem'] = own['inventory1']
		    own['inhand'] = 1
		    cont.activate(cont.actuators["R_Arm_0"])
		
		## Same as above, but for inventory slot 2  
	elif handslot == 2 and own['inhand'] != 2 and own['inventory2'] != "" and own['handitem'] == "":
		    equippingitem = inv2.children[0]
		    equippingitem.setParent(Rhand, 0, 1)
		    equippingitem.worldPosition = Rhand.worldPosition
		    equippingitem.worldOrientation = Rhand.worldOrientation
		    cont.activate(cont.actuators["R_Arm_1"])
		    own['handitem'] = own['inventory2']
		    own['inhand'] = 2
	elif handslot == 2 and own['inhand'] != 2 and own['inventory2'] == "" and own['handitem'] == "":
		    own['handitem'] = own['inventory2']
		    own['inhand'] = 2
		    cont.activate(cont.actuators["R_Arm_0"])
		#let the property know what the new active state of the hand is now that all items have been swapped.
def Vehicle(Eitem, Seat, headempty):
	unequipitem()
	Etext.visible = False
	own.setParent(Seat, 0, 1)
	own['Parent'] = Seat['Vehicle']
	print("Riding " + own['Parent'])
	cont.activate(cont.actuators["track2"])
	own.worldPosition = Seat.worldPosition
	own.worldOrientation = Seat.worldOrientation
	headempty.state = 2
	Eitem.state = 2
	own.state = 2
	
def ladder(Eitem, headempty):

	unequipitem()
	own.setParent(Eitem.parent, 0, 1)
	headempty.state = 2
	cont.activate(cont.actuators["R_Arm_1"])
	cont.activate(cont.actuators["L_Arm_1"])
	own.worldPosition = Eitem.worldPosition
	own.worldOrientation = Eitem.worldOrientation
	own['Parent'] = 'Ladder'
	Etext.visible = False
	own.state = 2

def flashlight():
	if cont.sensors["Mouseclick"].positive and own['FlashlightOn'] == False:
		own['FlashlightOn'] = True
	elif cont.sensors["Mouseclick"].positive and own['FlashlightOn'] == True:
		own['FlashlightOn'] = False





		######  END OF SWITCHING ITEMS IN HAND
		#flashlight off needs to be instant. flashlight on can be animated.
def inventory():
	if own['handitem'] == "Flashlight":
		flashlight()
	elif own['handitem'] != "Flashlight":
		own['FlashlightOn'] = False

		
	if own['handitem'] == 'Stick':
		pass
		
		
		
		

def talking():
	pass
	#if keyboard.events[bge.events.EKEY] == JUST_ACTIVATED and cont.sensors["NearConv"].positive and person['convnumber'] == 0:
	#			person['convnumber'] = 1
	#			bge.logic.globalDict['convnumber'] = person['convnumber']

			
def interact(Eitem):
	Etext.visible = True
	Etext['Text'] = Eitem['Interact'] + "(E)"
	if Eitem['Interact'] == 'Pick up':
		Etext.worldPosition = [Eitem.worldPosition[0], Eitem.worldPosition[1],Eitem.worldPosition[2]+2]
		if keyboard.events[bge.events.EKEY] == JUST_ACTIVATED:
			pickup(Eitem)
	elif Eitem['Interact'] == 'Drive':
		for Seat in Eitem.children:
			if 'Seat' in Seat:
				Etext.worldPosition = [Seat.worldPosition[0], Seat.worldPosition[1],Seat.worldPosition[2]+2]
				if keyboard.events[bge.events.EKEY] == JUST_ACTIVATED:
					Vehicle(Eitem, Seat, headempty)
	elif Eitem['Interact'] == 'Climb':
		Etext.worldPosition = [Eitem.worldPosition[0], Eitem.worldPosition[1],Eitem.worldPosition[2]+2]
		if keyboard.events[bge.events.EKEY] == JUST_ACTIVATED:
			ladder(Eitem, headempty)
		    
		    
		
			

			

def main():

		

	if keyboard.events[bge.events.QKEY] == JUST_ACTIVATED:
		pass

		#if player is near a pickup item, find out what he's picking up.


		
		#if mousewheel, find out what should go into his hand.
		
	inhand()
		# Inventory
	inventory()
	
	#print(own.children[0])

	if cont.sensors['NearE'].positive:
		Eitem = getEitem()
		interact(Eitem)
	elif not cont.sensors['NearE'].positive:
		Etext.visible = False

	if keyboard.events[bge.events.EKEY] == JUST_ACTIVATED:
	   own['prop'] = "My name is %s" % (name)
	   #talking()
		#if hes near a bike, activate riding a bike.		    
		#if keyboard.events[bge.events.EKEY] == JUST_ACTIVATED and own['bikeSit'] == False and cont.sensors["NearVehicle"].positive:
		    #ridebike()
		#if keyboard.events[bge.events.EKEY] == JUST_ACTIVATED and own['Ladder'] == False and cont.sensors["NearLadder"].positive:
		#   ladder()
		#it probably has to be with owner or parent commands
		#variable owna
		#own[prop]



main()
