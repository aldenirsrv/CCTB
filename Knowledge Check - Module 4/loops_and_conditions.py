# Practise Exercises
# 1. There are 2 sisters, Annie and Jane, born in 1996 and 1999 respectively. They want to know who was born in a leap year. Write an if-else statement to determine who was born in a leap year.¶

annie = 1996
jane = 1999
if annie % 4 == 0:
    print("Annie was born in leap year")
elif jane % 4 == 0:
    print("Jane was born in leap year")
else:
    print("None of them were born in a leap year")

# 2. In a school canteen, children under the age of 9 are only given milk porridge for breakfast. Children from 10 to 14 are given a sandwich, and children from 15 to 17 are given a burger. The canteen master asks the age of the student and gives them breakfast accordingly. Sam's age is 10. Use if-else statement to determine what the canteen master will offer to him.
# 9 only milk
# 10 to 14 sandwish
# 15 to 17 burger
given_age = 8
if given_age <= 9:
    print("Get your milk porridge for breakfast")
elif given_age >=10 and given_age <= 14:
    print("Get your sandwich")
elif given_age >=15 and given_age <= 14:
    print("Get your burger")
else:
    print("Are you a student?")



# Practise Exercises on Loops
# Write a for loop the prints out all the element between -5 and 5 using the range function.
for n in range(-5,5):
    print(n)
# Print the elements of the following list: Genres=[ 'rock', 'R&B', 'Soundtrack', 'R&B', 'soul', 'pop'] Make sure you follow Python conventions.
genres=[ 'rock', 'R&B', 'Soundtrack', 'R&B', 'soul', 'pop'] 
for genre in list(genres):
    print(genre)

# Write a while loop to display the values of the Rating of an album playlist stored in the list PlayListRatings. If the score is less than 6, exit the loop. The list PlayListRatings is given by: PlayListRatings = [10, 9.5, 10, 8, 7.5, 5, 10, 10]
playListRatings = [10, 9.5, 10, 8, 7.5, 5, 10, 10]
index = 0
while index < len(playListRatings) :
    rating = playListRatings[index]
    if rating < 6:
        break
    print(rating)
    
    index += 1


# Write a while loop to copy the strings 'orange' of the list squares to the list new_squares. Stop and exit the loop if the value on the list is not 'orange':
squares = ['orange', 'orange', 'purple', 'blue ', 'orange']
new_squares = []
index = 0
while index < len(squares):
    if squares[index] != 'orange':
        break
    new_squares.append(squares[index])
    index+= 1
   
print(new_squares)

# Your little brother has just learned multiplication tables in school. Today he has learned tables of 6 and 7. Help him memorise both the tables by printing them using <code>for</code> loop.

print("multiplication tables")

print("Table of 6")
for i in range(11):
    print(f"6 x {i} = {6*i}")\

print("\nTable of 7")
for i in range(11):
    print(f"7 x {i} = {7*i}")


# The following is a list of animals in a National Zoo. Animals = ["lion", "giraffe", "gorilla", "parrots", "crocodile","deer", "swan"]

# Your brother needs to write an essay on the animals whose names are made of 7 letters. Help him find those animals through a while loop and create a separate list of such animals.
animals = ["lion", "giraffe", "gorilla", "parrots", "crocodile","deer", "swan"]
made_of_seven = []
index = 0
while index < len(animals):
    if len(animals[index]) == 7:
        made_of_seven.append(animals[index])    
    index += 1
print(made_of_seven)