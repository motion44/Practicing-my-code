password = "baby"

while True:
    guess = input("Guess what the password is! ")
    if guess == password:
        print("Access Granted!")
        break
    else:
        print("Access Denied. Try Again!")
