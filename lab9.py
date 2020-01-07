##stranger_things = {}
##stranger_things["The Vanishing of Will Byers"] = "The Duffer Brothers"
##stranger_things["The Weirdo on Maple Street"] = "The Duffer Brothers"
##stranger_things["Holly, Jolly"] = "Shawn Levy"
##stranger_things["The Body"] = "Shawn Levy"
##stranger_things["The Flea and the Acrobat"] = "The Duffer Brothers"
##stranger_things["The Monster"] = "The Duffer Brothers"
##stranger_things["The Bathtub"] = "The Duffer Brothers"
##stranger_things["The Upside Down"] = "The Duffer Brothers"
##
##def episodes_directed(episodes_dict, director):
##    count = 0
##    for k in episodes_dict:
##        if(director == episodes_dict[k]):
##            count += 1
##    print(director + " directed " + str(count) + " episodes")
##
##episodes_directed(stranger_things, "The Duffer Brothers")
##episodes_directed(stranger_things, "Shawn Levy")
##episodes_directed(stranger_things, "Kerri Cobb")

class Series:

    def __init__(self, title, creator, seasons, episodes):
        self.title = title
        self.creator = creator
        self.seasons = seasons
        self.episodes = episodes

    def __str__(self):
        return self.title + " has aired " + str(self.episodes) + " episodes over " + str(self.seasons) + " seasons."
    def addSeason(self):
        self.seasons += 1

    def addEpisodes(self, new_episodes):
        self.episodes += new_episodes
        
stranger_things = Series("Stranger Things", "The Duffer Brothers", 1, 8)

print(stranger_things)
stranger_things.addSeason() # here comes the next season
stranger_things.addEpisodes(9) # there are now 9 more episodes
print(stranger_things)
