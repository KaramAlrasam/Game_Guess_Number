#import module randome and os
import os, random
#make class game
class game:
#make function for the combuter to choose random number
  def __init__(self):
    self.wrong_guesses=[]
    self.gusnum=0
  
#make comper function to discover the number less or greader 
  def  comper(self,i_com:int, i_us:int):
    if i_com<i_us:
      return("Your number is to HIGH than requested number")
    elif i_com==i_us:
      return True
    else:
      return( "Your number is to LESS than requested number")
#make function to work the game if he wants to play again
  def main(self):
    #make while loop to let the user quit or enter the game
    while True:
      choice=input("""
-----------------------------
    WELCOME TO OUR GAME
      GUSSING NUMBER
-----------------------------
1- start.
2- exit.

Choose number: """).strip()
      if choice=="1":
        self.clear_screan()
        
        self.playGame()
      elif choice=="2":
        self.clear_screan()
        print("Exiting...")
        break
      else:
        self.clear_screan()
        print("Invaled input enter number.")
        
  def playGame(self):
#give the user five tries if he doesn't ansewer will loss
    tries=7
    self.gusnum+=random.randint(0,101)
    del self.wrong_guesses[:]
    while tries!=0:
      try:
        u_guess=int(input("Guess the number of (1-100): ").strip())
        if  self.comper(self.gusnum, u_guess)==True:
          input("You win🎊🎉✨\n\npress enter to go to the main page")
          self.clear_screan()
          break
        elif self.comper(self.gusnum, u_guess)!=True and u_guess in self.wrong_guesses:
          self.clear_screan()
          print("You choose the number already, try again")
        else:
          tries-=1
          self.wrong_guesses.append(u_guess)
          self.clear_screan()
          print(self.comper(self.gusnum, u_guess))        
          print(f"You have {tries} tries")
      except ValueError:
        self.clear_screan()
        print("You must add number.")
      finally:
        if tries==0:
         
          input(f"You loss😭😭😭\nThe number was {self.gusnum}\n\npress enter to go to the main page")
          self.clear_screan()
    self.gusnum-=self.gusnum
  
#make clear_screen function
  def clear_screan(self):
    os.system("cls"if os.name=="nt"else "clear")
if __name__=="__main__":
  myGame=game()
  myGame.main()




