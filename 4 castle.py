import random
exitChoice = ""
while exitChoice != "EXIT":
    print("Create your character!")
    name = input("What is your character called?")
    age = input("How old is your character?")
    pronouns = input("What are your character's pronouns?")
    print("Your character's name is", name)
    print("Your character is", age, "years old")
    print("Your character's pronouns are", pronouns)
    print(name,"says, 'Thanks for creating me!'")
    print("You enter a dim room in a gloomy castle. The doors creak and outside the wind is howling.")
    print("In front of you are four doors. You must choose one.")
    playerChoice = input("Choose 1, 2, 3 or 4...")
    if  playerChoice == "1":
        print("You find a room full of treasure. Well done!")
        print("Congratulations, you win!")
    elif playerChoice == "2":
        print("The door opens and a hideous ogre attacks you!")
        print("Sorry, you're dead!")
    elif playerChoice == "3":
        print("You go into the room and find a sleeping dragon.")
        print("You can either:")
        print("1) Try to steal some of the dragon's gold.")
        print("2) Try to sneak around the dragon to the exit.")
        dragonChoice = input("Type 1 or 2...")
        if dragonChoice == "1":
            print("The dragon wakes up and eats you!")
            print("Game over, you lose.")
        elif dragonChoice == "2":
            print("You sneak around the dragon and escape the castle. You're rich!")
            print("Congratulations, you win!")
        else:
            print("Sorry, you didn't enter 1 or 2!")
    elif playerChoice == "4":
        print("You enter a room with a sphinx.")
        print("It asks you to guess what number it is thinking of, between 1 and 10.")
        number = int(input("What number do you choose?"))
        if number == random.randint(1,10):
            print("The sphinx hisses in disappointment. You guessed correctly.")
            print("She must let you go free.")
            print ("Congratulatioms, you win!")
        else:
            print("The sphinx tells you that your guess is incorrect.")
            print("She eats you!")
            print("Game over, you lose.")
            
    else:
        print("Erm, you didn't enter 1, 2, 3 or 4...")
    exitChoice = input("Press return to play again, or type EXIT to leave.")