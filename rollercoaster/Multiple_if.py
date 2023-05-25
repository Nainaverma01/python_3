print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
age = int (input("What is your age? "))
bill = 0
if height >= 120 :
  print ("You can ride the rollercoaster")
  if age < 12:
    bill = 5
    print ("Child tickets are $5.")
  elif age <= 18:
    print ("Youth tickets are $7.")
    bill = 7
  else :
    print ("Adult tickets are $12.")
    bill =12
  want_photo = input("Do you want a photo taken ? Y or N ")
  if want_photo == "Y" :
# bill = bill + 3 is same as bill +=3
    bill +=3
  print (f"Your final bill is ${bill} ")
else :
  print ("Sorry, You need to grow taller before you ride")
