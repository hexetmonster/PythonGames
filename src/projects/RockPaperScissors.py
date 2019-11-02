# Rock paper scissors game

import time as t
import random as r

CPU_Wins = 0
Player_Wins = 0
CPU_Losses = 0
Player_Losses = 0
Ties = 0

Games = 0

def Random(Min, Max):
  return r.randint(Min, Max)

def Game():
  global CPU_Wins, Player_Wins, CPU_Losses, Player_Losses, Games, Ties
  I = input("Play? (Y/N) ")
  if I.lower() == "n" or I.lower() == 'no':
    if Games > 0:
      print("")
      print("Player wins: {}, Player losses: {}".format(Player_Wins, Player_Losses))
      print("CPU wins: {}, CPU losses: {}".format(CPU_Wins, CPU_Losses))
      print("Ties: {}".format(Ties))
      print("")
    else:
      print("No wins/losses to track (no game was played)")
    print("------------------------------------------")
    print("Game ended")
    return
  I = input("Rock, paper, scissors? ")
  Rand = Random(1, 3)
  #print("Random: {}".format(Rand))
  
  YourChoice = ""
  CPUChoice = ""
  
  if I.lower() == 'rock':
  	YourChoice = 'rock'
  elif I.lower() == 'paper':
    YourChoice = 'paper'
  elif I.lower() == 'scissors':
    YourChoice = 'scissors'
  
  # Do CPU choices
  if Rand == 1:
    CPUChoice = 'rock'
  elif Rand == 2:
    CPUChoice = 'paper'
  elif Rand == 3:
    CPUChoice = 'scissors'
  
  # Combinations
  Result = ""
  if YourChoice == 'rock' and CPUChoice == 'rock':
    Result = 'tie'
  elif YourChoice == 'rock' and CPUChoice == 'paper':
    Result = 'CPUWin'
  elif YourChoice == 'rock' and CPUChoice == 'scissors':
    Result = 'PlayerWin'
  elif YourChoice == 'paper' and CPUChoice == 'rock':
    Result = 'PlayerWin'
  elif YourChoice == 'paper' and CPUChoice == 'paper':
    Result = 'tie'
  elif YourChoice == 'paper' and CPUChoice == 'scissors':
    Result = 'CPUWin'
  elif YourChoice == 'scissors' and CPUChoice == 'rock':
    Result = 'CPUWin'
  elif YourChoice == 'scissors' and CPUChoice == 'paper':
    Result = 'PlayerWin'
  elif YourChoice == 'scissors' and CPUChoice == 'scissors':
    Result = 'tie'
  
  if Result == 'tie':
    print("Game was a tie!")
    Ties = Ties + 1
  elif Result =='PlayerWin':
    print("Player wins")
    Player_Wins = Player_Wins + 1
    CPU_Losses = CPU_Losses + 1
  elif Result == 'CPUWin':
    print("CPU has won!")
    CPU_Wins = CPU_Wins + 1
    Player_Losses = Player_Losses + 1
  else:
    print("No one won!")
  
  Games = Games + 1
  
  Game()
Game()


