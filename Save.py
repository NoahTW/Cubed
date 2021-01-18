import bge



def firstsave():
        cont = bge.logic.getCurrentController()
        scene = bge.logic.getCurrentScene()
        print(bge.logic.globalDict['charactername'])
        bge.logic.globalDict['SavedGame'] = True
        print(bge.logic.globalDict['SavedGame'])
        bge.logic.globalDict['inventory1'] = ""
        bge.logic.globalDict['inventory2'] = ""
        
        bge.logic.globalDict['playerposx'] = scene.objects['Spawn1'].worldPosition.x
        bge.logic.globalDict['playerposy'] = scene.objects['Spawn1'].worldPosition.y
        bge.logic.globalDict['playerposz'] = scene.objects['Spawn1'].worldPosition.z
        cont.activate(cont.actuators['SaveData'])
        cont.activate(cont.actuators['State1'])

        

        
def savename():
  cont = bge.logic.getCurrentController()
  if cont.sensors['Mouse'].positive and cont.sensors['Mouse.001'].positive:
        bge.logic.globalDict['charactername'] = cont.owner['Text']
        bge.logic.globalDict['genderm'] = cont.owner['GenderM']
        


def checkpointsave():
        cont = bge.logic.getCurrentController()
        scene = bge.logic.getCurrentScene()
        print(bge.logic.globalDict['charactername'])
        bge.logic.globalDict['SavedGame'] = True
        print(bge.logic.globalDict['SavedGame'])
        
        

        
        
        #Inventory
        bge.logic.globalDict['inventory1'] = scene.objects['Player']['inventory1']
        bge.logic.globalDict['inventory2'] = scene.objects['Player']['inventory2']

        
        #Player's location
        bge.logic.globalDict['playerposx'] = scene.objects['Player'].worldPosition.x
        bge.logic.globalDict['playerposy'] = scene.objects['Player'].worldPosition.y
        bge.logic.globalDict['playerposz'] = scene.objects['Player'].worldPosition.z

        #Save the data, exit the save state
        cont.activate(cont.actuators['SaveData'])
        cont.activate(cont.actuators['State1'])



################scenario + character + conversationnumber + .py = scriptconversation