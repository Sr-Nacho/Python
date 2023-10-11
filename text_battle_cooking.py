"""
Conditionals (elif and else)
Instruction: Nested Conditionals
Part 2: Cooking
"""
import random
# Ask the user if they like to cook
cook = input("Do you like to cook? Enter y or n: ")

# If the user likes to cook, ask if they have a favorite dish
if cook == "y":
    favorite = input("Do you have a favorite dish? Enter y or n: ")

    # If the user has a favorite dish, ask them to share
    if favorite == "y":
        dish = input("What is your favorite dish to cook? ")

    # Print a message about the user cooking
    print("Pasta is my favorite dish to cook.")

# If the user doesn't like to cook, ask if they have a favorite restaurant
# Then, note the excellent use of comments from this point forward
else:
    favorite = input("Do you have a favorite restaurant? Enter y or n: ").lower()
    if favorite == "y":
        print("oh cool")
    if favorite == "n":
        print()
        print("You uncultured swine!")
        print("Now you shall perish!")
        print()
        print("Miles appears, and he is angry")
        print("Watch out for his piercing stare!")
        input("press enter to continue")
        print()
        alive = "yes"
        health = 20
        enemy_health = 1000
        while alive == "yes":
            print("You have " + str(health) + " health remaining")
            enemy_check = random.randint(1, 4)
            if enemy_check == 4:
                print("Miles has " + str(enemy_health) + " remaining")
                print("He feels you assessing him, and is judging you hevily.")
            elif enemy_check == 3:
                print("You can almost hear his meanacing presence as he conveys his hatred through pure willpower.")
                print('You hear in your head "IF THE TRUTH WILL KILL THEM LET THEM DIE".')
                print("he is speaking of the truth of your identity as a foodie, or lack thereof.")
                print("In summary, he hates you because you lack character in the realm of food.")
                print()
            elif enemy_check == 2:
                print("He sends the sound of bells into your head with his mind.")
                print("The resounding echos are destroying you from the inside and force you to confront your failures in life.")
                print()
            elif enemy_check == 1:
                print("You feel faint as you stand in his presence.")
                print()
            action = input("act/fight/item ").lower()
            if action == "fight":
                attack = int(input("Pick a number between 1 and 10 "))
                num = random.randint(1, 10)
                if attack != num:
                    enemy_health -= 5
                    print("You unleash a great swing of your sword.")
                    print("Miles takes 5 damage.")
                elif attack == num:
                    enemy_health -= 10
                    print("You feel extra powerful as you sink your sword into the flesh of your enemy.")
                    print("Critical hit!")
                    print("Miles takes 10 damage.")
            elif action == "act":
                print("Actions: Check health")
                act = input("Type one of the above actions " ).lower()
                print("You peer into the enemys soul, and with that you check his status")
                print("Miles has no intention of sparing you")
                print("Miles has " + str(enemy_health) + " health remaining")
            elif action == "item":
                print("You reach into your pockets, but they are empty")
            print()
            block = int(input("block with a number('1/2/3/4')"))
            block_num = random.randint(1, 4)
            if block != block_num:
                attack_dmg = random.randint(1, 5)
                health -= attack_dmg
                print("Block failed. You take " + str(attack_dmg) + " damage as Miles' stare pierces your chest")
            if block == block_num:
                lifesteal = random.randint(1, 5)
                health += lifesteal
                print("Block successful. You gain " + str(lifesteal) + " health.")
                print("As Miles' stare pierces your chest, you stare back with a matching intensity, stealing his own life force")
            print()
            if health <= 0:
                print("Ur dead")
                print("lolz git good scrub")
                print("I just totally broke your story immersion, didn't I")
                alive = "no"
            if enemy_health <= 0:
                print('"Ha Ha Ha! I have accomplished my goal!"')
                print("Miles disintegrates")
                print("It feels as though a heavy weight has been lifted off of your shoulders")
                print("In this moment, you come to realize your identity")
                print("You come to realize that you hated your old self, before the battle")
                print("You have a deep hatred of all who lack this great sense of self")
                print("Through this, you realize that you have become the very thing you sought to destroy")
                alive = "Yes!!! Now more than ever!"
