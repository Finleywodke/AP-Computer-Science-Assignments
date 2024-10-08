airplane_speed = int(input("What is the speed of the airplane in mph? "))
wind_speed = int(input("What is the speed of the wind in mph? "))

wind_direction = True
while True:
        choice = input("Is the wind coming from [Behind] the plane or in [Front] of the plane? ")
        if choice =='Behind':
            positive = True
            break
        if choice =='Front':
            positive = False 
            break

destination = input("What is your destination? ")
distance = int(input("What is the distance from the plane to the destination in miles? "))

while positive == True:
    print("You will arive at", (destination), "in", (round((distance/(airplane_speed + wind_speed)),2)), "hours")
    break
while positive == False:
    print("You will arive at", (destination), "in", (round((distance/(airplane_speed - wind_speed)),2)), "hours")
    break


#Boeing 747 can travel at 576 mph

