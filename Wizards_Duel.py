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


#----------------------------------------------------------------------
# Supplementary code (like generating instances of objects)



#----------------------------------------------------------------------
# Main Code
# Initializing game

starting_the_game()
my_name = input("What is your name? ")
sleep(2)
print("Hello {}! Welcome to Hogwarts. Before we can begin, I need some more information. ".format(my_name))
sleep(2)
