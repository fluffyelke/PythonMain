my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]      #copy all elements

print("My Favorite foods are:")
print(my_foods)

print("\nMyFriend's favorite foods are:")
print(friend_foods)


#prove the lists are different
my_foods.append('chicken')
friend_foods.append('pork')
print("My Favorite foods are:")
print(my_foods)

print("\nMyFriend's favorite foods are:")
print(friend_foods)
