print("Create your character!")
name = input("What is your character called?")
age = input("How old is your character?")
pronouns = input("What are your character's pronouns?")
strengths = input("What are your character's strengths?")
weaknesses = input("What are your chracter's weaknesses?")
print("Your character's name is", name)
print("Your character is", age, "years old")
print("Your character's pronouns are", pronouns)
print("Strengths:", strengths)
print("Weaknesses:", weaknesses)
print(name,"says, 'Thanks for creating me!'")

print("You enter a dim room in a gloomy castle. The doors creak and outside the wind is howling.")
print("In front of you are three doors. You must choose one.")
playerChoice = input("Type 1, 2 or 3...")
if  playerChoice == "1":
    print("You find a room full of treasure. Well done!")
    print("Congratulations, you win!")
elif playerChoice == "2":
    print("The door opens and a hideous ogre attacks you!")
    print("Sorry, you're dead!")
elif playerChoice == "3":
    print("You go into the room and find a sleeping dragon.")
    print("The dragon wakes up and eats you!")
    print("Game over, you lose.")
else:
    print("Erm, you didn't enter 1, 2 or 3...")
    print("Run the game again to have another go.")