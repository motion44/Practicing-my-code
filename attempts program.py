attempts = 3

while True:
    try:
        number = int(input("Choose a number: "))
    except ValueError:
        print("Invalid number!")
        attempts -= 1
        print(f"You have {attempts} attempts left")
        if attempts == 0:
            print("You have run out of attempts, try again later.")
            break
    else:
        if number > 0:
            print("Your number is positive.")
        elif number == 0:
            print("Your number is zero.")
        else:
            print("Your number is negative.")
        break
    finally:
        print("Attempt finished")
