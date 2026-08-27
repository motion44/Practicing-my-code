def do_math(x, y):
    result = x + y
    return result

while True:
    try:
        number = (input("Enter two numbers: "))
        number = number.split()
        x = int(number[0])
        y = int(number[1])
        answer = do_math(x, y)
        print(answer)
    except ValueError:
        print("That is not a valid number!")
