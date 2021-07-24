# https://docs.python.org/3/library/csv.html
import csv
# https://docs.python.org/3/library/os.html
import os

# 2d array - slot 0 = player's name, slot 1 = average, slot 2 - 6 = best scores
players_scores = []

# hard-coded file path
# score_file_path = "C:\\Users\\carol\\Desktop\\Sophomore Year\\TechnicalTest\\TechnicalTest\\Question2\\golf_scores.csv"

# relative file path
cur_wd = os.getcwd()
score_file_path = os.path.join(cur_wd, "Question2\\golf_scores.csv")

# helper function that appends scores to the correct player or creates a new player entry
def score_append(p, s):
    for player_record in players_scores:
        # if the player's record exists, append this score to the end of their record
        if player_record[0] == player:
            player_record.append(int(s))
            return;
    # otherwise, create a new record
    players_scores.append([p, 0, int(s)])

# read in the player and score data
with open(score_file_path, 'r') as scores:
    # ignore the first line
    scores.readline()
    # create csv reader
    scores_reader = csv.reader(scores, delimiter=',')
    # process each player and score
    for line in scores_reader:
        # split and store the player and score
        player = line[0]
        score = line[1]
        # if the score list is empty, create the first entry
        if not players_scores:
            players_scores.append([player, 0, int(score)])
        else:
            # sppend score to already populated score list
            score_append(player, score)

# calculate averages
for i in range(len(players_scores)):
    # if the player did not play five rounds, remove them
    if len(players_scores[i]) < 7:
        players_scores.pop(i)
    else:
        # if the player played more than five rounds, remove their worst scores
        while len(players_scores[i]) > 7:
            players_scores[i].remove(max(players_scores[i][2:]))
        # sum the player's five best scores
        sum = 0
        for j in range(2, len(players_scores[i])):
            sum += players_scores[i][j]
        # assign the average to the correct cell in the array
        players_scores[i][1] = float(sum / (len(players_scores[i]) - 2))

# sort using modified insertion sort
for k in range(1, len(players_scores)):
    # hold the current player record
    cur = players_scores[k]
    # hold their average score for comparison
    cur_avg = cur[1]
    j = k
    # navigate through the array and make appropriate swaps to sort
    while j > 0 and players_scores[j-1][1] > cur_avg:
        players_scores[j] = players_scores[j-1]
        j = j - 1
    players_scores[j] = cur

# print out rankings
for i in range(len(players_scores)):
    print(str(i+1) + ". " + str(players_scores[i][0]) + ": " + str(players_scores[i][1]))
