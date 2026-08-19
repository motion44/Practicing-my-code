total = 0

while True:
    number = input("Type in a number! ")
    if number == "done":
        print(total)
        break
    else:
         number = int(number)
         total += number
         print(total)
