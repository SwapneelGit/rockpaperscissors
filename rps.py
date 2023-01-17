import time
import random
def startbotplay():
  print("-----------------------------------")
  print(" Press 1 for Rock \n Press 2 for Paper \n Press 3 for Scissors")
  playinput=input()
  selectionlist=["Rock","Paper","Scissors","Rock","Paper","Scissors","Rock","Paper","Scissors","Rock","Paper","Scissors","Rock","Paper","Scissors","Rock","Paper","Scissors"]
  computermove=random.choice(selectionlist)
  if playinput=="1":
    if computermove=="Rock":
      print("Draw! Rock = Rock")
    elif computermove=="Scissors":
      print("You won! Rock > Scissors")
    elif computermove=="Paper":
      print("You Lost! Rock < Paper")
    else:
      print("Bot Error")
  elif playinput=="2":
    if computermove=="Rock":
      print("You won! Paper = Rock")
    elif computermove=="Scissors":
      print("You lost! Paper < Scissors")
    elif computermove=="Paper":
      print("Draw! Paper = Paper")
    else:
      print("Bot Error")
  elif playinput=="3":
    if computermove=="Rock":
      print("You lost! Scissors < Rock")
    elif computermove=="Scissors":
      print("Draw! Scissors = Scissors")
    elif computermove=="Paper":
      print("You won! Scissors = Paper")
    else:
      print("Bot Error")
  else:
    print("Input Error")
  print("-----------------------------------")
  playagain=input("Do you want to play again? \n Yes or No?")
  if playagain=="Yes":
    startbotplay()
  if playagain=="No":
    pass
def startlocalplay():
  print("-----------------------------------")
  print(" Press 1 for Rock \n Press 2 for Paper \n Press 3 for Scissors")
  time.sleep(1)
  playinput=input("Player 1 Move:")
  playinput2=input("Player 2 Move:")
  print("-----------------------------------")
  if playinput=="1":
    if playinput2=="1":
      print("Draw! Rock = Rock")
    elif playinput2=="3":
      print("Player 1 won! Rock > Scissors")
    elif playinput2=="2":
      print("Player 2 won! Rock < Paper")
    else:
      print("Bot Error")
  elif playinput=="2":
    if playinput2=="1":
      print("Player 1 won! Paper < Rock")
    elif playinput2=="3":
      print("Player 2 won! Paper < Scissors")
    elif playinput2=="2":
      print("Draw! Paper = Paper")
    else:
      print("Bot Error")
  elif playinput=="3":
    if playinput2=="1":
      print("Player 2 won! Scissors < Rock")
    elif playinput2=="3":
      print("Draw! Scissors = Scissors")
    elif playinput2=="2":
      print("Player 1 won! Scissors = Paper")
    else:
      print("Bot Error")
  else:
    print("Input Error")
  print("-----------------------------------")
  playagain=input(" Do you want to play again? \n Yes or No?")
  if playagain=="Yes":
    startlocalplay()
  if playagain=="No":
    pass
print(" Welcome to RockPaperScissors")
print(" 1) Play with Computer")
print(" 2) Local Multiplayer")
gamemode=input()
if gamemode=="1":
  startbotplay()
elif gamemode=="2":
  startlocalplay()
