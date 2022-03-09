#Tip Calculator project

#This is my welcom message for my user's
print("Welcome to Shaqtv's tip calculator\n")

#I created a variable called bill to recevie the bill total
bill = float(input("What was the total bill? $\n"))

#I created a variable called tip to recevie the tip amount
tip =int(input("How much would you like to tip?\n"))

#I created a variable called people to recevie the amount of people that would be spliting the bill
people = int(input("How many people to split the bill?\n"))

#I wanted to get the tip as a percentage
tip_as_percent = tip / 100

#I multiplied the bill by the tip percentage to get the total tip amount
total_tip_amount = bill * tip_as_percent

#I got the totol tip amout plus the bill to get the total amount
total_amount = bill + total_tip_amount

#varible for 10% tax
unc_sam = 10 /100

#I added the 10 percent tax to the total amount
taxed_bill = total_amount + unc_sam

#I divided the bill by the amount of people
bill_per_person = taxed_bill / people

#I rounded the bill to the second places
final_amount = round(bill_per_person, 2)


#printed the final amount with a message 
print(f"Each person should pay: ${final_amount}")