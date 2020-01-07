import numpy as np

#----------------------------------------------
# CSCI 127 Program 5
# November 21 2017
# Tyler Bourgeois
#----------------------------------------------

class Person():
#initialize an object called Person and set its first and last names
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

#return the first and last name of the person in a string
    def get_name(self):
        return self.first_name + " " + self.last_name
    
#returns first name of the person    
    def get_first_name(self):
        return self.first_name
    
#returns last name of the person
    def get_last_name(self):
        return self.last_name
        
class Batter(Person):
#initialize an object called Batter that inherents the Person class with the addition of storing
#their position, at bats, and hits
    def __init__(self, first_name, last_name, position):
        Person.__init__(self, first_name, last_name)
        self.position = position
        self.at_bats = 0
        self.hits = 0

#returns position of batter
    def get_position(self):
        return self.position

#returns at bats of batter
    def get_at_bats(self):
        return self.at_bats

#returns hits of batter
    def get_hits(self):
        return self.hits

#adds to the total number of at bats of the Batter
    def set_at_bats(self, at_bats):
        self.at_bats += int(at_bats)

#adds to the total number of hits by the batter
    def set_hits(self, hits):
        self.hits += int(hits)
        
#prints the formatted info of the batter            
    def __str__(self):
        if(self.at_bats != 0):
            return "{:<24} {}".format((self.get_first_name() + " " + self.get_last_name() + "(" + self.position + ")"),
                                  (str(round(self.hits/self.at_bats, 3)) + " (" + str(self.hits) + " for " + str(self.at_bats) + ")"))
        else:
            return "{:<24} {}".format((self.get_first_name() + " " + self.get_last_name() + "(" + self.position + ")"),
                                  ("0.000" + " (" + str(self.hits) + " for " + str(self.at_bats) + ")"))
    
class All_Batters():
#initializes a numpy array to store the names of all of the batters
    def __init__(self,batterArray):
        self.batters = np.array(batterArray)

#returns the numpy array of all of the batters
    def get_all_batters(self):
        return self.batters
     
def main():
    batterInfo = open("batting.txt", "r") #opens file to be read by the program
    tempArray = batterInfo.read().splitlines() #splits each line of the file into an array
    batterInfoArray = []  #temp array to contain the arrays of the array InfoArrayTemp

    #iterates through the lines of the text file and stores them in the batterInfoArray
    for i in range(len(tempArray)):
        batterInfoArray.append(tempArray[i].split(","))
    #creates a person object with each name found in the file
    AllBattersTemp = []
    for a in range(int(batterInfoArray[0][0])):
        person = Person(batterInfoArray[a+1][0], batterInfoArray[a+1][1])
        AllBattersTemp.append(person)
    allBatters = All_Batters(AllBattersTemp)

    #creates batter objects with the names previously found and also stores their position
    AllBattersTemp = []
    print("{:<24} {}".format("Player", "Batting Average") + "\n----------------------------------------")
    for name in All_Batters.get_all_batters(allBatters):
        for i in range(int(batterInfoArray[0][0])):
            if (str(batterInfoArray[i+1][0] + " " + batterInfoArray[i+1][1]) == str(name.get_name())):
                batter = Batter(name.get_first_name(), name.get_last_name(), batterInfoArray[i+1][2])
                AllBattersTemp.append(batter)
        print(batter)
    allBatters = All_Batters(AllBattersTemp)

    #totals the at bats and hits for each batter for each game and sets the values in their respective batter objects
    print("{:<24} {}".format("Player", "Batting Average") + "\n----------------------------------------")
    for name in All_Batters.get_all_batters(allBatters):
        for i in range(len(batterInfoArray) - 6):
            if str(batterInfoArray[i+6][0] + " " + batterInfoArray[i+6][1]) == str(name.get_name()):
                name.set_at_bats(batterInfoArray[i+6][3])
                name.set_hits(batterInfoArray[i+6][4])
        print(name)

    

main()
