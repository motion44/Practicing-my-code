health = 10
1 = take_damage
2 = heal

while health > 0:
    
    number = input("Choose a number between 1 and 2")
    number = int(number)
    
    if number != 1 and number != 2:
        print("You chose the wrong number!")
    
    if number == 1:
        choice = input("How much damage?")
        choice = int(choice)
        health = health - choice
        print(f"Your health is now {health}")
    
    elif number == 2:
        heal = input("How much heal?")
        heal = int(heal)
        health = health + heal
        if health > 10:
            print("Your health bar is full!")
        else:
            print(f"Your health is now {health}")
    
    if health <= 0:
        print("Game Over!")
