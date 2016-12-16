food = "banana bread"
print (food.capitalize())

print "*" + food.center(25) + "*"
print "*" + food.ljust(25) + "*"
print "*" + food.rjust(25) + "*"

print food.find("e")
print food.find("na")
print food.find("b")

print food.rfind("e")
print food.rfind("na")
print food.rfind("b")

print food.index("e")

fruit = "Banana"
sz = len(fruit)
lastch = fruit[sz-1]
print lastch