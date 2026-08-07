'''
#calculate the innings of a batsman to count the number of boundaries,runs and dots

runs = list(map(int, input("Enter runs: ").split(',')))

score = 0
boundaries = 0
dots = 0

for i in runs:
    score = score + i

    if i == 4 or i == 6:
        boundaries = boundaries + 1

    if i == 0:
        dots = dots + 1

print("Total Score:", score)
print("Boundaries:", boundaries)
print("Dot Balls:", dots)

'''

'''
#Phone unlock system
password = "1203"
chance = 5

while chance > 0:
    user = input("Enter Password: ")

    if user == password:
        print("Phone Unlocked")
        break
    else:
        chance = chance - 1
        print("Wrong Password")
        print("Chances Left:", chance)

if chance == 0:
    print("Phone Locked")

'''
'''
#ATM pin entery
pin = "1234"
chance = 3

while chance > 0:
    user_pin = input("Enter ATM PIN: ")

    if user_pin == pin:
        print("PIN Correct")
        break
    else:
        chance = chance - 1
        print("Wrong PIN")
        print("Chances Left:", chance)

if chance == 0:
    print("ATM Card Blocked")



'''









