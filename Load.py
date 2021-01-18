import bge

bge.logic.globalDict['SavedGame'] = False
bge.logic.globalDict['worldjumping'] = False
bge.logic.globalDict['playerposx'] = bge.logic.getCurrentScene().objects['Spawn1'].worldPosition.x
bge.logic.globalDict['playerposy'] = bge.logic.getCurrentScene().objects['Spawn1'].worldPosition.y
bge.logic.globalDict['playerposz'] = bge.logic.getCurrentScene().objects['Spawn1'].worldPosition.z
#bge.logic.globalDict['CharacterOrientation'] = bge.logic.getCurrentScene().objects['Spawn1'].worldOrientation





def loadgame():
    cont = bge.logic.getCurrentController()
    if cont.sensors['MouseOver'].positive and cont.sensors['MouseClick'].positive and bge.logic.globalDict['SavedGame'] == True:
        print("LoadGame", bge.logic.globalDict['SavedGame'])
        print("Loading")
        cont.activate(cont.actuators['LoadStatePlayer'])
        cont.activate(cont.actuators['State1'])
    elif cont.sensors['MouseOver'].positive and cont.sensors['MouseClick'].positive:
        cont.activate(cont.actuators['Nope.aviVis'])
        cont.activate(cont.actuators['Nope.aviState'])


def loaddata():
    bge.logic.getCurrentController().activate(bge.logic.getCurrentController().actuators['LoadData'])


def menuorload():
    cont = bge.logic.getCurrentController()
    if bge.logic.globalDict['worldjumping'] == False:
        cont.activate(cont.actuators['MenuCamState'])
        cont.activate(cont.actuators['MenuState'])
    if bge.logic.globalDict['worldjumping'] == True:
        cont.activate(cont.actuators['LoadState'])
        cont.activate(cont.actuators['State1'])







