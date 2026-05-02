import random

enemy_health = 10
player_health = 10

print("Guess a random number from 1 to 5! If you guess right, you deal damage to the enemy, and if the enemy guesses right, he deals damage to you! Good luck and have fun!")


while enemy_health > 0 and player_health > 0:
    
    number = random.randint(1, 5)
    guess = input("Type in a number from 1 to 5: ")
    guess = int(guess)
    
    if guess == number:
        print("You guessed the right number! The enemy has lost 3 hp!")
        enemy_health = enemy_health - 3
    else:
        print("You guessed wrong! You still dealt 1 hp point of damage however.")
        enemy_health = enemy_health - 1
        
    enemy_number = random.randint(1, 5)
    enemy_guess = random.randint(1, 5)
    if enemy_guess == enemy_number:
        print("The enemy has guessed right! You have lost 3 hp!")
        player_health = player_health - 3
    else:
        print("The enemy has guessed wrong! You have lost 1 hp!")
        player_health = player_health - 1
        
    print(f"Your health is {player_health}")
    print(f"Enemy's health is {enemy_health}")

    if enemy_health <= 0:
        print("The game is over! You have defeated the enemy!")
        break
    elif player_health <= 0:
        print("Game over! You have been defeated!")
        break
