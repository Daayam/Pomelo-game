# Wizards Duel
# This is a test 2
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


