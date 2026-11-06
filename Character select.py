#Inspired by Bleach Anime and Xenoverse 2 story mode concept

import random

print("Welcome to the Bleach inspired character customization\n")

chatbotd1 = ["Nice choice!", "This really suits you.", "I see the vision!", "What a suprise!?"]
chatbotd2 = ["I could see this", "Versatile pick..", "A lot of potential!"]

#Character Customization 

count = 1
MFSelect = ["Male", "M", "Female", "F"]

name = input("Enter your name: ")
M_or_F = input("Male or Female: ").strip().title()

while M_or_F not in MFSelect:
  print("Invalid Input! **PLEASE ENTER (Male, M, Female, or F.)**")
  M_or_F = input("Male or Female: ").strip().title()

faction = input("Pick your path (Shinigami, Hollow, Quincy, Human, Fullbringer): ")

def opts():
    if faction == "Hollow" or faction == "hollow":
        print("Your heart is filled with Darkness")
    elif faction == "Quincy" or faction == "quincy":
        print("Monk of Destruction!")
    elif faction == "Human" or faction == "human":
        print("Pure soul..")
    elif faction == "Fullbringer" or faction == "fullbringer":
        print("Hidden Potential... seek knowledge to unleash it")
        if faction == "Shinigami" or faction == "shinigami":
            print("Prideful Hero")
opts()

Affiliation = input("\nPick an affiliation(Soul Society,Hueco Mundo *Espada*, Wandenreich *Sternritters*, WOTL, No Affiliation): ")



