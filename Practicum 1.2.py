scores = [0,31,27,31,49,21,17,25]

wins = 0
losses = 0

for i in range(0, len(scores), 2):
    if(scores[i] > scores[i+1]):
        wins += 1
    elif(scores[i] < scores[i+1]):
        losses += 1
print("MSU has",wins,"win(s)","and",losses,"loss(es)")
