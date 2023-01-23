import os, time

health = 100
sword = False
explosives = False
key = False

def startGame():
  os.system('clear') # clear the screen for the player
  print("Welcome to the Maze Escape Game!")
  print("You find yourself trapped in a maze and must find a way out.")
  print()
  print()
  print("Let's get started!")
  time.sleep(5) # wait 3 seconds before moving on
  Maze1() # runs to send the player to cave #1

def Maze1():
  global sword # use the sword variable from the top
  os.system('clear')
  if sword:
    print("You are in the first part of the Maze cave. Would you like to take the path to your left or to your right?")
  else:
    print("You are in the first part of the Maze. There is a sword on the ground, and a path to your left, and a path to your right. What would you like to do?")
  decision = input(">>").strip().lower()
  if decision.find("sword") > -1:
    print("Picking up the sword.")
    sword = True
    time.sleep(3)
    Maze1()
  elif decision.find("left") > -1:
    print("You tried to cut through the wall of the Maze and it was too dense.")
    time.sleep(3)
    Maze1()
  elif decision.find("right") > -1:
    print("you cut through the wall on the right.")
    time.sleep(3)
    Maze2()
  else:
    print("Sorry, that command is not found.")
    time.sleep(3)
    Maze2()

def Maze2():
  global explosives, health
  os.system('clear')
  if explosives:
    print("Welcome to the 2nd part of the Maze. You see a gloomy light to right of you and darkness to the left. Which way do you want to go?")
  else:
    print("Welcome to the 2nd part of the Maze. You've found a crate of explosives on the ground and pick them up. You see a gloomy light to the right of you and darkness to the left. Which way do you want to go?")
  decision = input(">>").strip().lower()
  if decision.find("explosives") > -1:
    print("Picking up crate of explosives.")
    explosives = True
    time.sleep(3)
  elif decision.find("right") > -1:
    print("You see a gloomy light to right of you and decide to walk to it unfortunately the light gets too bright and you die.")  
    time.sleep(3)
    Maze2()
  elif decision.find("left") > -1:
    print("As you walk into the darkness eyes appear in the distance and you throw your explosives at only to figure out that you killed a ogre.")
    time.sleep(3)
    Maze3()
  else:
    print("Sorry, that command is not found.")
    time.sleep(3)
    Maze3()

def Maze3():
  global key, health
  os.system('clear')
  if key:
    print("You've made it to the 3nd part of the Maze. You once again have the choice of going right or left, both ways lead to a door. Which door will it be? ")
  else:
    print("You've made it to the 3nd part of the Maze. As you were walking you found a key sticking out of the ground. You once again have the choice of going right or left, but this time they both lead to doors. Which door will it be?")
  decision = input(">>").strip().lower()
  if decision.find("key") > -1:
    print("Picking up key.")
    key = True
    time.sleep(3)
  elif decision.find("left") > -1:
    print("You choose the door to the left. You put the key in the key hole and turn. The door opens and to your suprise you see a room with nothing in it. You walk in, but its a trap, the door slams shut and the walls start moving closer together till you are crushed to death (like star wars).")  
    print()
    print()
    print()
    time.sleep(3)
    Maze3()
  elif decision.find("right") > -1:
    print("You choose the door to the right. You put the key in the key hole and turn. The door opens and you see the exit. You sprint through the door to freedom.")
    print()
    print()
    print()
    time.sleep(3)
    endGame()
  else:
    print("Sorry, that command is not found.")
    time.sleep(3)
    endGame()
  pass

def endGame():
  os.system("clear")
  print("Congratulations victory is yours!!!!!")
  pass

startGame()