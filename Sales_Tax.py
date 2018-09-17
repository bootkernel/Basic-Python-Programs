#Sales Tax
#Asks the user to input total sales for the month

def sales_tax():
      ask_month = input("Enter the month: ")
      ask_total_sales = float(input("Enter the total sales for "+ ask_month))


      statetax = ask_total_sales*5/100 #5percent state tax
      countytax = ask_total_sales*2.5/100 #2.5percent county tax
      get_totalsales_tax = statetax + countytax #total sales tax
      print("The amount of state sales tax: ", statetax)    
      print("The amount of county sales tax: ", countytax)
      print("The amount of total sales tax: ", get_totalsales_tax)

sales_tax()
import Main

