# ---------------------------------------
# CSCI 127, Joy and Beauty of Data
# Program 1: GPA Calculator 
# Tyler Bourgeois
# Last Modified: September 13, 2017 
# ---------------------------------------
# This program caluclates the GPA of a student of Montana State University.
# It takes an input of the total number of classes as well as the letter grade
# and credits in each class.
# ---------------------------------------
classes = input("Enter the number of courses you are taking: ")
print()
gradelist = []
creditlist = []

def translate(lettergrade):
    if (lettergrade in("A","a")):
        return 4.0
    elif (lettergrade in("A-","a-")):
        return 3.7
    elif (lettergrade in("B+","b+")):
        return 3.3
    elif (lettergrade in("B","b")):
        return 3.0
    elif (lettergrade in("B-","b-")):
        return 2.7
    elif (lettergrade in("C+","c+")):
        return 2.3
    elif (lettergrade in("C","c")):
        return 2.0
    elif (lettergrade in("C-","c-")):
        return 1.7
    elif (lettergrade in("D+","d+")):
        return 1.3
    elif (lettergrade in("D","d")):
        return 1.0
    elif (lettergrade in("F","f")):
        return 0.0
    else:
          pass
        
def calculategpa():
    top = 0
    bottom = 0
    for j in range(0, int(classes)):
        top = (float(gradelist[j]) * float(creditlist[j])) + float(top)
        bottom = float(creditlist[j]) + float(bottom)

    return (top / bottom)

for i in range(1, int(classes) + int(1)):
    
    currentgrade = input("Enter grade for course " + str(i) + ": ")
    credit = input("Enter credits for course " + str(i) + ": ")
    gradelist.append(translate(currentgrade))
    creditlist.append(int(credit))
    print()
    
print("Your GPA is " + '{:01.2f}'.format(calculategpa()))
