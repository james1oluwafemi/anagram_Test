shop_List = ["milk", "milo", "tooth paste", "tooth brush", "detergent", "bath soap", "morning fresh", "tissue", "water", "deodorant", "socks"]

# number 1 - create a shopping list
print(shop_List)

# number 2 - number of items in shopping list
print(len(shop_List))

# number 3 - slice out priority items 
print(shop_List[2:9])

# number 5 - add an item to shopping list
shop_List.append("bread (for Tunde)")
print(shop_List)

# number 4 - add "bought" to each item in shopping list
print([item + " bought" for item in shop_List])
