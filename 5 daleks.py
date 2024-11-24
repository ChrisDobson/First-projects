daleks = 2
password = "password"
print("Quickly! Daleks are invading the planet.")
print("You need to activate the global defence platforms.")
print("I hope you know the password, for Earth's sake...")
print()
print("--------------------------------------------------")
print("       WELCOME TO THE GLOBAL DEFENCE NETWORK      ")
print("--------------------------------------------------")
print()

guess = input("Please enter the password: ").upper()

while guess != password:
    print()
    print("INCORRECT PASSWORD.")
    print()

    daleks = daleks ** 2
    print("There are", daleks, "daleks now on Earth. Try again!")

    if daleks > 7400000000:
        break

    print()
    print("Password hint: it's their favourite word!")
    guess = input("Quick! Please enter the password: ").upper()

if daleks > 7400000000:
    print("Oh no! The Daleks have outnumbered us. All is lost!")
else:
    print("Hurray, we won the fight and the world is saved!")