#Learn from men with hair on their chest. CGMasters.net
import bge


cont = bge.logic.getCurrentController()
scene = bge.logic.getCurrentScene()
own = cont.owner

keyboard = bge.logic.keyboard
JUST_ACTIVATED = bge.logic.KX_INPUT_JUST_ACTIVATED

def main():
  if keyboard.events[bge.events.BKEY] == JUST_ACTIVATED:
    scene.addObject("Bike1", own, 0)
main()
