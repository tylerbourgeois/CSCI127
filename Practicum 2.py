##score_differences = {}
##score_differences["October 14, 2017"] = 8
##score_differences["OCtober 14, 2017"] = -12
##score_differences["October 21, 2017"] = 3
##
##wins = 0
##losses = 0
##
##for score in score_differences:
##    if(score_differences[score] > 0): wins += 1
##    elif(score_differences[score] < 0): losses += 1
##
##print(wins, "wins -", losses, "losses")    

class Appliance():
    def __init__(self,manufacturer):
        self.manufacturer = manufacturer

class Refrigerator(Appliance):
    def __init__(self, manufacturer, cooling_agent):
        Appliance.__init__(self, manufacturer)
        self.cooling_agent = cooling_agent

    def __str__(self):
        return "The " + self.manufacturer + " refrigerator contains refrigerant " + self.cooling_agent

my_refrigerator = Refrigerator("Samsung", "R134a")
print(my_refrigerator)
