# Here we will use Multiple IF and if/elif/else to play around treasure building game.
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇
cross_road = input ('You\'re at a cross road. Where do you want to go? Type "left" or "right" \n').lower()
if cross_road == "left" :
  lake = input('Great ! Now you are at sea. We have a temple at shore ? what you want to do? "swim" or "boat" for ride? \n').lower()
  if lake == "boat" :
    door = input("You reached The Temple. What amongst the three door of house you wanna enter? 'Red' 'Yellow' or 'Green'?\n").lower()
    if door == "red" :
      print("Game Over.Its a lava room.")
    elif door == "yellow" :
      print ("WOW! You have found the treasure. You win SAILOR.")
    elif door == "green" :
      print ("Game Over. You have been bitten by a deadly snake.")
    else :
      print ("Bad Choice. You are now falling forever.Game Over")    
  else :
    print ("Game Over.You are eaten by my shark.")    
else :
  print("Game Over.You fell into a hole.")


