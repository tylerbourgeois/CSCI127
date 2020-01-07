# ---------------------------------------
# CSCI 127, Joy and Beauty of Data
# Program 3: Pokedex
# Tyler Bourgeois
# Last Modified: 10/15/2017
# ---------------------------------------
# This program, given a pokedex with values number, name, hp, and type(s), can do
# various different operations. They are: printing all pokemon in the pokedex with their info,
# looking up a pokemon by their name and printing their info, looking up a pokemon
# by their number and printing their info, printing the total number of pokemon in the pokedex,
# and printing the total number of hitpoints of all the pokemon
# ---------------------------------------

# Your solution goes here ...

# imports python string module for usage later
import string

# prints the menu of all operations that the program can preform
def printMenu():
    print("1. Print Pokedex\n2. Lookup Pokemon by Name\n3. Lookup Pokemon by Number\n4. Print Number of Pokemon\n5. Print Total Hit Points of All Pokemon\n6. Quit\n")

# prints the info of all pokemon in the pokedex
def printPokedex(pokedex):
    print("\nThe Pokedex\n-----------")
    for pokemon in pokedex:   
        printPokemonInfo(pokedex,pokemon)
        print("-----------")
    print()

# prints how many pokemon are in the pokedex
def howManyPokemon(pokedex):
    print("There are " + str(len(pokedex)) + " different Pokemon\n")

# prints how many total hitpoint
#
#
# s the pokemon in the pokedex have
def howManyHitPoints(pokedex):
    hitpoints = 0
    for pokemon in pokedex:
        hitpoints += pokedex[pokemon][1]
    print("The total number of hit points for all Pokemon is " + str(hitpoints) + "\n")

# given a name, prints the info of the pokemon
def lookupByName(pokedex, name):
    if(name in [i for j in pokedex.values() for i in j]):
        namedex = {}
        for i in range(1,len(pokedex)+1):
            namedex[pokedex[i][0]] = i
        pokemon = namedex[name]
        printPokemonInfo(pokedex,pokemon)
    else:
        print("The pokemon named " + name + " does not exist")
    print()

#prints the info of a pokemon given its number   
def lookupByNumber(pokedex, pokemon):
    if(pokemon in pokedex):
        printPokemonInfo(pokedex,pokemon)
        print()
    else:
        if(str(pokemon).isdigit()):
            print("Error: Pokemon number " + str(pokemon) + " does not exist\n")
        else:
            print("That is not a number, try again")
        
# Gets the type of the pokemon requested
def getType(pokedex,pokemon):
    if(len(pokedex[pokemon]) > 3): pokemon_type = pokedex[pokemon][2] + " and " + pokedex[pokemon][3]
    else: pokemon_type = pokedex[pokemon][2]
    return pokemon_type

# Prints the formatted information of a pokemon
def printPokemonInfo(pokedex,pokemon):
    print("Number:" + str(pokemon) + ", Name: " + pokedex[pokemon][0] + ", HP: " + str(pokedex[pokemon][1]) + ", Type: " + getType(pokedex,pokemon))
# ---------------------------------------
# Do not change anything below this line
# ---------------------------------------

# creates the pokedex dictionary from the pokedex.txt file
def createPokedex(filename):
    pokedex = {}
    file = open(filename, "r")
    
    for pokemon in file:
        pokelist = pokemon.strip().split(",")
        index = int(pokelist.pop(0))
        pokedex[index] = [pokelist.pop(0)]          # name
        pokedex[index] += [int(pokelist.pop(0))]    # hit points
        pokedex[index] += [pokelist.pop(0)]         # type
        if len(pokelist) == 1:
            pokedex[index] += [pokelist.pop(0)]     # optional second type

    file.close()
    return pokedex

# ---------------------------------------

# checks to see if a menu input is valid
def getChoice(low, high, message):
    legal_choice = False
    while not legal_choice:
        legal_choice = True
        answer = input(message)
        for character in answer:
            if character not in string.digits:
                legal_choice = False
                print("That is not a number, try again.")
                break 
        if legal_choice:
            answer = int(answer)
            if (answer < low) or (answer > high):
                legal_choice = False
                print("That is not a valid choice, try again.")
    return answer

# ---------------------------------------

# main function that processes an input during the menu 
def main():
    pokedex = createPokedex("pokedex.txt")
    choice = 0
    while choice != 6:
        printMenu()
        choice = getChoice(1, 6, "Enter a menu option: ")
        if choice == 1:    
            printPokedex(pokedex)
        elif choice == 2:
            name = input("Enter a Pokemon name: ")
            name = name.capitalize()
            lookupByName(pokedex, name)
        elif choice == 3:
            number = getChoice(1, 1000, "Enter a Pokemon number: ")
            lookupByNumber(pokedex, number)
        elif choice == 4:
            howManyPokemon(pokedex)
        elif choice == 5:
            howManyHitPoints(pokedex)
    print("Thank you.  Goodbye!")

# ---------------------------------------

main()
