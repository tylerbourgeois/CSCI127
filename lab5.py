#1

import statistics

numbers = [0,1]
print(statistics.median_low(numbers))
print(statistics.median(numbers))

#2

def count_characters(stringlist):
    count = 0
    for i in range(len(stringlist)):
        for j in range(len(stringlist[i])):
            count += 1
    return count

print(count_characters(["You", "may", "say", "I'm", "a", "dreamer"]))                

#3

def my_reverse(stringlist):
    count = 0
    newlist = []
    for i in range(len(stringlist)):
       newlist.append(stringlist[len(stringlist) - 1 - count])
       count += 1
    return newlist

print(my_reverse(["You", "may", "say", "I'm", "a", "dreamer"]))
        
        
def create_file(file_name, n):
    outfile = open(file_name, "w")
    for i in range(1, n + 1):
        outfile.write(str(i) + "\n")
    outfile.close()
create_file("jbd.txt", 5)
        
