length = int(input("What is the length of your turf field in feet? " ))
width = int(input("What is the width of your turf field in feet? "))
cost_per_square = int(input("What is the cost per square foot of your turf field? $"))

area = (length * width)
perimeter = ((length * 2)+(width *2))
total_cost = (area * cost_per_square)

print("Area =", (area), "ft^2")
print("Perimeter =", (perimeter), "ft")
print("Total Cost = $" + str(total_cost))