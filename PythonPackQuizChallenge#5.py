print("You have a 10 foot pvc pipe to make a triangular banner for a lemonade stand.")
cut1 = int(input("How far down should the first cut be made in feet? "))
cut2 = int(input("How far down should the second cut be made in feet? "))

(L1) = cut1
(L2) = (cut2 - cut1)
(L3) = (10 - L2 - L1)

print("length 1 = " + str(L1))
print("length 2 = " + str(L2))
print("length 3 = " + str(L3))

import math

#Use Heron's formula
print("The area will be " + (str(math.sqrt(5*(5-L1)*(5-L2)*(5-L3)))) + "ft^2")