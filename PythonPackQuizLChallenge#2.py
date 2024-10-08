#MadLibs Story - Once upon a time, in the land of (location), there was a (Occupation)(1) who was looking for a (Object)(1).
# But on his way towards the (another location), he was met be a mysterious figure who was holding a (weapon). The figure began
# to shout "(phrase)" at the man as he (past tense verb) towards him. The (Occupation)(1) (action) away from the shadowy figure and grabbed
# a (object_2) and threw it at the man and hit him straight in the (body part). The figure collapsed and turned into (type of liquid) as the
# treasure that the (Occupation)(1) was looking for had appeared at last, a legendary (Object)(1). The (Occupation)(1) would then go on to
# save all of the townspeople by using the (Object)(1) to (action_2). The end.

location_1  = input("Name a location ")
occupation = input("Name an occupation ")
obj_1 = input("Name a random object ")
obj_2 = input("Name another random object ")
location_2 = input("Name a place of business ")
weapon = input("Name a weapon ")
phrase = input("Write a phrase ")
past_tense_verb = input("Give a past-tense verb ")
action_1 = input("Name an escape action in past-tense ")
body_part = input("Name a body part ")
liquid = input("Name a liquid ")
food = input("Name a food ")
action_2 = input("Name another action ")

print ("Once upon a time, in the land of", (location_1), "there was a", (occupation), "who was looking for a", str(obj_1)+".")
print ("But on his way towards a", str(location_2)+",", "he was met be a mysterious figure who was holding a", str(weapon)+"."+" The figure began")
print ("to shout,", "'"+ str(phrase)+"'", "at the man as he", (past_tense_verb), "towards him. The", (occupation), (action_1), "away from the shadowy figure and grabbed")
print ("a", (obj_2), "and threw it at the man and hit him straight in the", (body_part)+"." " The figure collapsed and turned into", (liquid), "as the")
print ("treasure that the", (occupation), "was looking for had appeared at last, a legendary", (obj_1)+"." " The", (occupation), "would then go on to")
print ("save all of the townspeople by using the", (obj_1), "to", (action_2)+".","The end.")
