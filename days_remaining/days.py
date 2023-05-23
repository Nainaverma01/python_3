age = input("What is your current age? ")
#we consider out age to be an integer rather than a float(decimal)
age_as_int = int(age)
#suppose you are going to live till 90 years
years_remaining = 90 - age_as_int
remain_day = str(years_remaining*365)
remain_week = str(years_remaining*52)
remain_mon = str(years_remaining*12)
message = f"You have {remain_day} days, {remain_week} weeks, and {remain_mon} months left."
#printing the message
print (message)
