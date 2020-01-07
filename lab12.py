import numpy as np
import matplotlib.pyplot as plt

# -----------------------------------------------------
# CSCI 127, Lab 12
# November 21, 2017
# Tyler Bourgeois
# -----------------------------------------------------

def read_file(name):
    input_file = open(name, "r")
    number_buckets = int(input_file.readline())
    total_counties = int(input_file.readline())

    county_populations = np.zeros([total_counties], dtype="int")
    for county_number in range(total_counties):
        line = input_file.readline().split(",")
        county_populations[county_number] = int(line[1])
    county_populations.sort()
    input_file.close()

    return number_buckets, county_populations

# -----------------------------------------------------

def print_summary(averages):
    print("Population Grouping Summary")
    print("---------------------------")
    for grouping in range(len(averages)):
        print("Grouping", grouping + 1, "has a population average of",
              averages[grouping])

# -----------------------------------------------------
# Do not change anything above this line
# -----------------------------------------------------

def calculate_averages(number_buckets, county_populations):
    n = county_populations.size / number_buckets
    temp_array = np.split(county_populations, number_buckets)
    averages = np.array([],dtype=int)
    for i in temp_array:
        sum_of_array = np.sum(i)
        average = sum_of_array / n
        average = int(average)
        averages = np.append(averages, average)
    return averages
          

# -----------------------------------------------------

def graph_summary(averages):
    x_data = np.arange(1,len(averages)+1,dtype=int)
    x_max = len(averages)
    plt.figure(num='CSCI 127, Lab 12')
    plt.plot(x_data, averages, '--c', x_data, averages, 'hb')
    plt.xticks(x_data)
    plt.xlabel('County Groupings')
    plt.ylabel('County Population Average')
    plt.title('Montana County Population Analysis')
    plt.show()

# -----------------------------------------------------

number_buckets, county_populations = read_file("montana-counties.txt")
averages = calculate_averages(number_buckets, county_populations)
print_summary(averages)
graph_summary(averages)
