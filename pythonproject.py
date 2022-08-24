import random
print("Welcome to Tom Nook's 2022 store management program created by AJ Slowey")
print("------------------------------------------------------------------------")
print("Please select a program of your choice:")
print("[A]: Income Tax Calculator")
print("[B]: Create an Employee Account")
print("[C]: Please End the Program")
selection = input("Please type your choice of A, B, or C: ")
answer = "A"
answer2 = "B"
answer3 = "C"
if selection == answer:
     print("Welcome to the Income Tax Calculator.")
     while True:
         try:
             print("What is your annual income in USD?")
             yearincome = input("Annual income: ")
             income = int(yearincome)
             totaltax = str(0.04 * income)
             print("You can expect to owe a total of " + totaltax + " dollars this year.")
             break
         except:
             print("Please enter a valid amount.")
elif selection == answer2:
 print("Welcome. Let's create an employee account.")
 first = input("Please type your first name: ")
 last = input("Please type your last name: ")
 username = first[0]+first[1]+first[2]+last[0]+last[1]+last[2]+last[3]
 print("The employee username will be " + username)
 number = random.randint(10,100)
 value = str(number)
 list = ["isabelle","sprinkle","frobert","anicotti","kkslider"]
 character = random.choice(list)
 print("Your password will be: "+ value + character)
elif selection == answer3:
 print("The program will now end.")
 print("Goodbye")
else:
 print("That is not a valid answer. Please close the program and hit F5 to restart.")




 
