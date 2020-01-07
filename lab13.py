import random
import numpy as np
import matplotlib.pyplot as plt

def generateCard():
    number = random.randint(1,13)
    if number == 13:
        value = "Ace"
    elif number == 12:
        value = "King"
    elif number == 11:
        value = "Queen"
    elif number == 10:
        value = "Jack"
    elif number < 10:
        value = number
    return value

def calculateCardValue(card,isFirstCard):
    if(card == "Ace"):
        return 11
    elif(card == "King" or card == "Queen" or card == "Jack"):
        return 10
    else:
        return card + 1
        
def calculate_score(cardOne, cardTwo):
    if(cardOne == "Ace" and cardTwo == "Ace"):
        return 12
    else:
        cardOneValue = calculateCardValue(cardOne,True)
        cardTwoValue = calculateCardValue(cardTwo,False)
        return cardOneValue + cardTwoValue

def plotData(dataArray):
    x_ticks = np.arange(np.amin(dataArray),np.amax(dataArray)+1, dtype="int")
    x_bins = np.arange(np.amin(dataArray),np.amax(dataArray)+2, dtype="int")
    plt.figure(num="CSCI 127, Lab 13")
    plt.xlabel("Hand Value")
    plt.ylabel("Probability")
    plt.xticks(x_ticks)
    plt.title("Histogram of BlackJack Hands")
    plt.grid()
    plt.hist(dataArray, bins = x_bins, density = "True", align = "left", color = "g", )
    plt.show()
  
def generateHands(hands):
    totalScoreArray = np.zeros([hands], dtype = "int")
    for i in range(hands):
        cardOne = generateCard()
        cardTwo = generateCard()
        totalScoreArray[i] = calculate_score(cardOne, cardTwo)
    plotData(totalScoreArray)
    
    
def main(hands):
    generateHands(hands)
    
main(10000)
