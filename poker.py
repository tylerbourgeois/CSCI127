# prints the heading and then the hand in the output file
def print_hand(hand, outputfile):
    outputfile.write("Poker Hand\n----------\n")
    for i in range(3):
        outputfile.write("Card " + str(i+1) + ": " + str(hand[i][0]).title() + " of " + str(hand[i][1]).title() + "\n")
 
    outputfile.write("\n")

# evaluates if the hand is a flush, three of a kind, two of a kind, or none of the previous three
# and prints it to the output file
def evaluate(hand, outputfile):
    evaluation = ""
    if flush(hand):
        evaluation = "FLUSH"
    elif three_of_a_kind(hand):
        evaluation = "THREE OF A KIND"
    elif two_of_a_kind(hand):
        evaluation = "TWO OF A KIND"
    else:
        evaluation = "NOTHING"
        
    outputfile.write("Poker Hand Evaluation: " + evaluation + "\n\n")

#evaluates if all three of the suites of the cards in the
#hand are the same and returns if it is true or not
def flush(hand):
    return hand[0][1] == hand[1][1] and hand[1][1] == hand[2][1]
#evaluates if all three of the ranks in the hand are the same
#and returns if it is true or not
def three_of_a_kind(hand):
    return hand[0][0] == hand[1][0] and hand[1][0] == hand[2][0]
#evaluates if just two of the ranks in the hand are the same
#and returns if it is true or not
def two_of_a_kind(hand):
    return hand[0][0] == hand[1][0] or hand[0][0] == hand[2][0] or hand[1][0] == hand[2][0]

# --------------------------------------
# Do not change anything below this line
# --------------------------------------

#takes each line from the input file and creates a list called "hand_as_list" for each hand using the format
#[['Rank 1','Suit 1'], ['Rank 2','Suit 2'], ['Rank 3','Suit 3']]
def main(poker_input, poker_output, cards_in_hand):    

    for hand in poker_input:
        hand = hand.split()
        hand_as_list = []
        for i in range(cards_in_hand):
            hand_as_list.append([hand[0], hand[1]])
            hand = hand[2:]
        print_hand(hand_as_list, poker_output)
        evaluate(hand_as_list, poker_output)

# --------------------------------------

#opens the input and output file to be read and written by this program
poker_input = open("poker.in", "r")
poker_output = open("poker.out", "w")

main(poker_input, poker_output, 3)

poker_output.close()
