print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
age = int (input("What is your age? "))
if height >= 120 :
  print ("you can ride the rollercoaster")
  if age <= 18:
    print ("PLease pay $7.")
  else :
    print ("Please pay $12.")
else :
  print ("Sorry, You need to get taller to ride")
