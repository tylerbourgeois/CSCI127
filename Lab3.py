# --------------------------------------
# CSCI 127, Lab 3
# September 19, 2017
# Tyler Bourgeois
# --------------------------------------

def count_vowels(sentence):
    return sentence.count("a") + sentence.count("e") + sentence.count("i") + sentence.count("o") + sentence.count("u") 

def count_vowels_iterative(sentence):
    count = 0
    for i in ("a" , "e", "i", "o", "u"):
        count += sentence.count(i)
    return count

def count_vowels_recursive(sentence):
    if not sentence:
        return 0
    return (1 if sentence[0] in "aeiou" else 0) + count_vowels_recursive(sentence[1:])
        
    

# --------------------------------------

def main():
    answer = "yes"
    while (answer == "yes") or (answer == "y"):
        sentence = input("Please enter a sentence to evaluate: ")
        sentence = sentence.lower()     # convert to lowercase
        print()
        print("Number of vowels using count     =", count_vowels(sentence))
        print("Number of vowels using iteration =", count_vowels_iterative(sentence))
        print("Number of vowels using recursion =", count_vowels_recursive(sentence))
        print()
        answer = input("Would you like to continue: ").lower()
        print()

# --------------------------------------

main()
