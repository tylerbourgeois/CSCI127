# --------------------------------------
# CSCI 127, Lab 4
# September 26, 2017
# Your Name
# --------------------------------------

def process_season(season, games_played, points_earned):
    print("Season: " + str(season) + ", Games Played: " + str(games_played) +
          ", Points earned: " + str(points_earned))
    print("Possible Win-Tie-Loss Records")
    print("-----------------------------")
    maxwins = points_earned / 3
    maxwins = int(maxwins)
    for i in range(maxwins+1):
        ties = (points_earned - (maxwins*3))
        if(ties<0): ties = 0;
        losses = games_played - maxwins - ties
        if(losses < 0): losses = 0
        if((maxwins+ties+losses) == games_played): print(str(maxwins) + "-" + str(ties) + "-" + str(losses))
        maxwins = maxwins-1
    print()

# --------------------------------------

def process_seasons(seasons):
    season = 0
    for i in range(len(seasons)):
        season += 1
        games_played = seasons[i][0]
        points_earned = seasons[i][1]
        process_season(season, games_played, points_earned)
        
# --------------------------------------

# format of list: [[season-1-games, season-1-points], [season-2-games, season-2-points], etc.]
soccer_seasons = [[1, 3], [1, 1], [1, 0], [2, 3], [2, 4], [10, 15], [10, 16], [10, 17]]

process_seasons(soccer_seasons)
