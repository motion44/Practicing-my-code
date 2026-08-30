while True:
    try:
        number = int(input("Choose a number: "))
 
    except ValueError:
        print("Thats not a valid number! ")
        pass
    else:
        if number > 0:
            print("Your number is positive.")
        elif number == 0:
            print("Your number is zero.")
        else:
            print("Your number is negative.")
        break
    finally:
        print("Program finished.")
