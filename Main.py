#******************************#
##Name: Subhajeet Mukherjee##
#*****************************#

#THIS IS THE MAIN PROGRAM

def main(): #defining main
      #asks the user to choose his/her preferred modules
      print("a. Rainfall\nb. Sales Tax\nc. Age\nd. Exit the Program") #lists all modules and options
      user_choose = input("Please choose an option from the list above: ") #input from the user

      if user_choose == "a" or user_choose == "A":                                  #condition
           import Rainfall
      elif user_choose == "b" or user_choose == "B":                              #condition                          
            import Sales_Tax
      elif user_choose == "c" or user_choose == "C":                             #condition
            import Age
      elif user_choose == "d" or user_choose == "D":                             #condition
            import sys
            sys.exit()
      else:
            print ("Invalid Choice")                                                                        #invalid choice condition
                                                                                                                                      # if the user inputs other keys instead of (A-E)

main() #calling main

