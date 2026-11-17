bill=float(input("What is your bill amount? "))
tip_percentage=float(input("What percentage would you like to tip? "))
no_people=int(input("How many people to split the bill? "))

tip=bill*tip_percentage/100
total=bill+tip
split_amt=total/no_people

print(f"Each has to pay ${split_amt:.2f}")
