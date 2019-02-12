class Type:
    def __init__(self, curry, burger, pizza, chinese):
        self.curry = curry
        self.burger = burger
        self.pizza = pizza
        self.chinese = chinese


class Item:
    def __init__(self, desc, price, avail):
        self.price = price
        self.desc = desc
        self.avail = avail
pepperoni = Item("Pepperoni Pizza", "£15", "True")
korma= Item("Chicken Korma", "£9", "False")
cburger= Item("Cheeseburger", "£7.50", "True")
ramen = Item("Ramen noodles", "£3.75", "True")



menuSelect = input("Choose your option: \n A) Pepperoni pizza \n B) Chicken korma \n C) Cheeseburger \n D) Ramen noodles")

while menuSelect == "a" or "b" or "c" or "d":
    cartConfirm = input("Would you like to place item in cart? Press 'Y' for yes and 'N' for no")
else:
    print ("Invalid option. Please select an option")
    

if cartConfirm == "y" or "Y":
    print("item added")
    
if continueShop == "y" or "Y":
    menuSelect = input("A) Pepperoni pizza, \n B) Chicken korma, \n C) Cheeseburger, \n D) Ramen noodles")
else:
    print ("Invalid option. please try again")
    continueShop = input ("would uoi like to continue")


