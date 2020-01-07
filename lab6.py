# --------------------------------------
# CSCI 127, Lab 6
# October 9, 2017
# Tyler Bourgeois
# --------------------------------------

def process_season(season, games_played, points_earned,scores_output):
    scores_output.write("Season: " + str(season) + ", Games Played: " + str(games_played) +
          ", Points earned: " + str(points_earned) + "\nPossible Win-Tie-Loss Records" +
            "\n-----------------------------\n")
    maxwins = points_earned / 3
    maxwins = int(maxwins)
    for i in range(maxwins+1):
        ties = (points_earned - (maxwins*3))
        if(ties<0): ties = 0;
        losses = games_played - maxwins - ties
        if(losses < 0): losses = 0
        if((maxwins+ties+losses) == games_played): scores_output.write(str(maxwins) + "-" + str(ties) + "-" + str(losses) + "\n")
        maxwins = maxwins-1
    scores_output.write("\n")

# --------------------------------------

def process_seasons(seasons,scores_output):
    for i in range(0, len(seasons)):
        games_played = seasons[i][0]
        points_earned = seasons[i][1]
        process_season(int(i+1), games_played, points_earned,scores_output)
        
# --------------------------------------

def main(scores_input,scores_output):
    scores_as_list = []
    for scoreset in scores_input:
        scoreset = scoreset.split()
        for i in range(1):
            scores_as_list.append([int(scoreset[0]), int(scoreset[1])])
            scoreset = scoreset[2:]
    process_seasons(scores_as_list,scores_output)
               


scores_input = open("soccer-in.txt", "r")
scores_output = open("soccer-out.txt" , "w")

main(scores_input, scores_output)

scores_input.close()
scores_output.close()
