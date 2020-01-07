#imports the pandas module to modify and read data structures and matplotlib to graph data
import pandas as pd
import matplotlib.pyplot as plt

#reads the contents of buildings.csv
buildings = pd.read_csv('buildings.csv')

plt.figure("Buildings Data")#sets the name of the window

plt.subplot(121) #creates subplots so two graphs can be on the same page
plt.title("Buildings by Building Classs") #sets the title of the graph
#graphs the construction class data in a pie chart by its class
buildings["Construction Class"].value_counts().plot(kind="pie", legend = True,autopct="%.2f",subplots = True)


#calcualtes the age of the buildings
for i in range(len(buildings)):
    year = buildings.ix[i, "Year Built"]
    year = 2017 - year
    buildings.ix[i, "Year Built"] = year

plt.subplot(122)
plt.xlabel("Age")#sets the x label of the plot
plt.ylabel("Frequency")#sets the y label of the plot
plt.title("Frequency of Ages of Buildings")#sets the title of the plot
buildings["Year Built"].value_counts(sort=False).plot.bar(color="c")#plots the ages of the buildings in a bar graph
plt.show()#shows the plots
