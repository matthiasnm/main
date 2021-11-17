#Budget code———

#What is the monthly budget?
budget= int(input("Hello what is your monthly budget? (NUMBERS ONLY NO COMMAS): "))
print("Your budget is: ")
print(budget)
#How much did you spend?
spent= int(input("How much did you spend?\n")) 
#Spent = 1 
#Did you spend any more ? yes/no to continue 
while True:
    cont= input('Did you spend anymore money? Yes or No\n')
    spenta= int(input("How much did you spend?\n")) 
    if cont == "no":
      break 

print("this works")
#(Loops until no)
#If continued 
#How much did you spend?
#Spent = 2 
#Did you spend anymore?
#No 
#Budget = this amount. 
