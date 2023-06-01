print("Welcome to my computer quiz!")   

playing = input("Do you want to play? ")

if playing != "Yes":
    quit()

print("Okay! Let's play :)")
score = 0

answer = input("Who is the GOAT of TENNIS? ")
if answer == "Roger Federer":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What is Bryce's favorite song atm? ")
if answer == "Waves of Blue":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("Socks on or off while you sleep? ")
if answer == "Off":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("Are you awesome? ")
if answer == "Obviously":
    print('Correct!')
    score += 1
else:
    print("You are awesome stop lying")

print("You got", score, "questions correct!")
print("You got", score/4 * 100, "%.")
#the top method is cleaner, and you dont have to include spaces
print("You got " + str(score) + " questions correct!")
print("You got " + str((score / 4) * 100) + "%.")

