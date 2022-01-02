print("Welcome to my virtual quiz!")

playing = input("Do you want to play? ")

if playing.upper() != "YES":
    quit()

print("Okay! Let's play :)")
score = 0

answer = input("What does CPU stand for? ")
if answer.upper() == "CENTRAL PROCESSING UNIT":
    print('Correct!')
    score += 1
else:
    print("Incorrect loser!")

answer = input("What does GPU stand for? ")
if answer.upper() == "GRAPHICS PROCESSING UNIT":
    print('Correct!')
    score += 1
else:
    print("Incorrect loser!")

answer = input("What does RAM stand for? ")
if answer.upper() == "RANDOM ACCESS MEMORY":
    print('Correct!')
    score += 1
else:
    print("Incorrect loser!")

answer = input("What does PSU stand for? ")
if answer.upper() == "POWER SUPPLY":
    print('Correct!')
    score += 1
else:
    print("Incorrect loser!")
print('\n')
print("You got " + str(score) + " questions correct!")
print("You got " + str((score / 4) * 100) + "% score")