#Age
#Asking the user to put his/her age

def Age():
      name = input("Type his/her name (Required to display full information: ")
      ask_user_age = float(input("Enter a person's age: "))

      if ask_user_age <= 1:
            print(name," is an infant")
      elif ask_user_age > 1 and ask_user_age < 13:
            print(name," is a child") 
      elif ask_user_age >= 13 and ask_user_age <20:
            print(name," is a teenager")
      elif ask_user_age >= 20:
            print(name," is an adult")
      else:
            print("Invalid Info")
Age()
import Main


