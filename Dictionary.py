my_dic = {"football":"A ball used to play football","basketball":"A ball used to play basketball","cricketball":"A ball used to play cricket"}
print(my_dic)

# add a new value pair to the dictionary
my_dic["volleyball"]="A ball used to play volleyball" 
print()
print(my_dic)

# Update a value in the dictionary
my_dic["football"]="A round ball with hexagons shapes on it"
print()
print(my_dic)

# Deleting a key value pair from the dictionary
my_dic.pop("basketball")
print()
print(my_dic)
# print the value with the help of the key
print()
print(my_dic["cricketball"])

# Check if the key exist in the dictionary
if "football" in my_dic:
    print("The word is in the dictionary")

else:
    print("The word is not in the dictionary")
    




