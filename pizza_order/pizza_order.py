# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
# extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆
small_pizza = 0
medium_pizza = 0
large_pizza = 0
#Write your code below this line 👇

if size == "S":
    small_pizza = 15
    if add_pepperoni == "Y":
        small_pizza += 2
    print (f"Your final bill is: ${small_pizza} ")
elif size == "M":
    medium_pizza = 20
    if add_pepperoni == "Y":
        medium_pizza += 2
    print (f"Your final bill is: ${medium_pizza} ")    
elif size == "L":
    large_pizza = 25
    if add_pepperoni == "Y":
        large_pizza += 2
    print (f"Your final bill is: ${large_pizza} ")
