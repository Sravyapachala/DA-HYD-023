'''
secret_number = 25

while True:
    guess = int(input("Enter the secret number: "))

    if guess == secret_number:
        print("Your guess is correct!")
        break
    else:
        print("Wrong code")

'''

'''
correct_otp = 1234
attempts = 0

while attempts < 7:
    otp = int(input("Enter OTP: "))

    if otp == correct_otp:
        print("OTP verified successfully!")
        break
    else:
        print("Wrong OTP")
        attempts += 1

if attempts == 7:
    print("You have exceeded 7 attempts.")


'''

'''
count = 0

while True:
    order = input("Enter your order: ")

    if order.lower() == "exit":
        break

    print("Order received:", order)
    count += 1

print("Total orders:", count)

'''

secret_name = "html"
chances = 3

while chances > 0:
    name = input("Enter the secret name: ")

    if name.lower() == secret_name:
        chances -= 1
        print("You won the game!")
        print("Chances remaining:", chances)
        break
    else:
        chances -= 1
        print("Wrong name")
        print("Chances remaining:", chances)

if chances == 0 and name.lower() != secret_name:
    print("You lost the game!")
    print("Chances remaining: 0")





























