password = "baby"
attempts = 0

while True:
    guess = input("Guess what the password is! ")
    if guess == password:
        print("Access Granted!")
        break
    else:
        print("Access Denied. Try Again!")
        attempts = attempts + 1
        if attempts == 3:
            print("Access LOCKED! Too many wrong attempts!")
            break
