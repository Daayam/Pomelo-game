# Wizards Duel
# 
from time import sleep
from random import choice, choices, randint
import os
clear = lambda: os.system ('cls' if os.name=='nt' else 'clear') #cls for windows, clear for linux

#-----------------------------------------------------------------------------------
# Define Classes

class Spell:
    def __init__(self, name, power, type_of_spell, effect, probability, sub_type = "None"):
        self.name = name
        self.power = power
        self.type = type_of_spell
        self.sub_type = sub_type
        self.effect = effect
        self.probability = probability

class Wand:
    def __init__(self, wood, core, power = 50, loyalty = 50, owner = None):
        self.wood = wood
        self.core = core
        self.power = power
        self.loyalty = loyalty
        self.owner = owner # will be used to link each instance of a wand to its respective character
        self.spells = {} # a dictionary of spells known(keys) and their probabilities. (values)

    def loyalty_attribute (self): # a class method to let the user know how loyal their wand is.
        if self.loyalty >= 100:
            print("Your wand believes in you completely. it will listen to you everytime.")
        elif self.loyalty >= 80:
            print("Your wand is loyal to you.")
        elif self.loyalty >= 60:
            print("Your wand is loyal to you.")
        elif self.loyalty >= 40:
            print("Your wand is somewhat loyal to you.")
        elif self.loyalty >= 5:
            print("Your wand is not loyal to you.")
        elif self.loyalty >= 0:
            print("Your wand completely distrusts you. It will not listen to you.")
        else:
            print("Probably best to change your wand....")
    
    def increase_loyalty(self, loyalty = 5):
        if self.loyalty <= 95 and self.loyalty >= 5:
            self.loyalty += loyalty
        else:
            pass
   
class Potion:
    def __init__(self, name, value, type_of_potion, effect):
        self.name = name
        self.value = value
        self.type = type_of_potion
        self.effect = effect

class Character:
    def __init__(self, name, house = "not sorted", year = 1, wand = None, health = 100):
        self.name = name
        self.house = house
        self.year = year
        self.wand = wand
        self.health = health
        self.potions_inventory = {}
        self.secret_skill = []
        self.status_effect = []
    
    def bond_wand(self, chosen_wand):
        self.wand = chosen_wand
        chosen_wand.owner = self
        if chosen_wand.core == "Dragon Heartstring":
            chosen_wand.power += 15
        if chosen_wand.core == "Unicorn Hair":
            chosen_wand.loyalty += 15


# ---------------------------------------------------------------------
# Game Mechanics



# ---------------------------------------------------------------------
# Dialogue and Scenes

def starting_the_game():
    print("This is Hogwarts Wizarding Duel— a harry potter themed game for personal use. It is an object based text game. You will be able to duel with unique characters, spells and potions. You can also play the game in story mode (future update) or in Duelling mode. Over time more updates may be added.")
    sleep(1)
    print("please wait")
    sleep(6)
    print("While playing this game, you may need to press enter to continue.")
    input("Press enter to continue")
    sleep(1)
    print("Sometimes you may have to wait a few seconds before pressing enter.")
    sleep(3)
    input("Press enter to start the game")
    clear ()

def run_tutorial():
    print("This is a turn based text game where you battle an opponent in a wizarding duel. Before you start {name}, you will have to create a character and a wand. When creating your character, you will be able to choose your year, and house.".format(name = my_name))
    sleep(2)
    input("")
    print("Your year corresponds to the difficulty setting of the game. In 2nd year, you will have basic functionality and limited spells. It is a great way to understand the mechanics of duelling. In 3rd year, you will be able to play the game with full functionality and many spells. It will give you a balanced experience. In 4th year, you will have access to full functionality, increased difficulty, and even more spells.")
    sleep(2)
    input("")
    print("There are 4 houses at Hogwarts: Gryffindor, Hufflepuff, Ravenclaw, and Slytherin. Each house will also have a secret skill based on their values. Gryffindor values bravery and strength. Hufflepuff values justice and loyalty. Ravenclaw values wit and learning. Slytherin values ambition and cunning. The house you pick will have an impact on your gameplay experience.")
    sleep(2)
    input("")
    print("After creating your character, you must obtain a wand. Your wand will have a wooden body, a magical core, a certain ammount of power, and some loyalty for you. {name}, they say the wand chooses the wizard. However, Ollivander has a surplus of wands in stock and you will be able to ask for your preferred core. Ollivander will be able to give you a wand with either Dragon Heartstring or Unicorn Hair. Dragon Heartstring wands tend to have more power, and Unicorn hair wands tend to be more loyal. Unfortunately, Phoenix feather wands are currently out of stock.".format(name = my_name))
    sleep(3)
    input("")
    print("When dueling, the objective is to beat the opponent, and the duel ends when a character loses all their health. On your turn, you will be able to cast a spell, or use a potion*. Each spell has a name, a power value, a type, an effect and a probability of successfully casting. *You cannot use potions in 2nd year.")
    sleep(3)
    input("")
    print("Your spells will also depend on your wand. The amount of damage dealt will depend on the power of the spell and the STRENGTH of your wand. As you use a spell, you will start to MASTER it and get better at casting it. The more loyalty your wand has, the more likely it is to listen to you. As you win duels, your LOYALTY will increase. In higher years, you will have to be more strategic, and will have to use every tool to your ADVANTAGE.")
    sleep(2)
    input("")
    print("\n", "\n", "\n") # adds 3 new lines

#----------------------------------------------------------------------
# Supplementary code (like generating instances of objects)

flipendo = Spell("Flipendo", 20, "offensive", "A basic dueling spell that knocks the target backwards.", 0.8)
protego = Spell("Protego", 20, "shield", "A basic sheild charm used to deflect spells.", 0.8)
stupefy = Spell("Stupefy", 20, "stun", "A basic duelling spell that stuns the opponent.", 0.6)
glacius = Spell("Glacius", 30, "status", "A spell that inflicts frost damage.", 0.5)

second_year_spells = [flipendo, protego, stupefy, glacius] #spells usable in second year
third_year_spells = second_year_spells #3rd and 4th year support will be added in a future update
fourth_year_spells = second_year_spells

#----------------------------------------------------------------------
# Main Code
# Initializing game

starting_the_game()
my_name = input("What is your name? ")
sleep(2)
print("Hello {}! Welcome to Hogwarts. Before we can begin, I need some more information. ".format(my_name))
sleep(2)
while True: # Run tutorial
    tutorial_input = ("Have you played this game before? ").title()
    if tutorial_input == "Yes": # This skips the tutorial
        break
    if tutorial_input == "No":
        sleep(1)
        run_tutorial()
        break
    else:
        print("I did not understand that. Please enter Yes or No")
        continue

#--------------------------
# Creating Characters

while True: # Choose house and year
    while True: # year
        chosen_year = int(input("What year are you in? (2, 3 or 4) "))
        if chosen_year == 2 or 3 or 4:
            break
        else:
            print("You are either in 2nd, 3rd, or 4th year. Try again.")
            continue
    chosen_house = input("What house are you in? (Gryffindor, Hufflepuff, Ravenclaw, or Slytherin) ").title()
    if chosen_house == "Gryffindor":
        house_skill = "Godrick's Might"
        wand_wood = "Cypress" # brave, bold, self-sacrificing
        break
    if chosen_house == "Hufflepuff":
        house_skill = "Helga's Allegiance"
        wand_wood = "Rowan" # For the clear deaded and pure hearted
        break
    if chosen_house == "Ravenclaw":
        house_skill = "Rowena's Mastery"
        wand_wood = "Beech" # Not for narrow minded and intolerant
        break
    if chosen_house == "Slytherin":
        house_skill = "Salazar's Advantage"
        wand_wood = "Vine" #
        break
    else:
        print("please check your spelling and try again.")
        continue

my_character = Character(my_name, chosen_house, chosen_year)
print("{name}, you are a {house} in year {year}.".format(name = my_name, house = chosen_house, year = chosen_year))
sleep(2)
input("")

while True: #Choose wand core
    chosen_core = input("What core would you like for your wand? (Dragon Heartstring wands are more powerful and Unicorn Hair wands are more loyal) ").title()
    if chosen_core == "Dragon Heartstring":
        break
    if chosen_core == "Unicorn Hair":
        break
    else:
        print("Dragon Heartstring or Unicorn Hair. Please check your spelling and try again.")
        continue
my_wand = Wand(wand_wood, chosen_core)
print("{name}, you are a {house} in year {year} and have a {wood} wand with a {core} core.".format(name = my_name, house = chosen_house, year = chosen_year, wood = wand_wood, core = chosen_core))
my_character.bond_wand(my_wand)
my_wand.loyalty_attribute()
my_character.wand.learn_spell()
sleep(5)
input("")
print("Now that we have enough information, we can proceed.")
sleep(2)
input("")
