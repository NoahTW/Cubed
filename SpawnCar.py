#This script runs on the large vehicle garage in the game, and will spawn the hovercar when run
import bge


cont = bge.logic.getCurrentController()
scene = bge.logic.getCurrentScene()
own = cont.owner

keyboard = bge.logic.keyboard
JUST_ACTIVATED = bge.logic.KX_INPUT_JUST_ACTIVATED

def main():
  if keyboard.events[bge.events.CKEY] == JUST_ACTIVATED:
    scene.addObject("Car1", own, 0)
main()
