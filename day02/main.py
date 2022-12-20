# A = rock; B = paper; C = scissors; X = rock; Y = paper; Z = scissors
hand_list = ["A", "B", "C"]
outcome_list = ["X", "Y", "Z"]
win_matrix = [["A", "Y"], ["B", "Z"], ["C", "X"]]
lose_matrix = [["A", "Z"], ["B", "X"], ["C", "Y"]]
# X = lose; Y = draw; Z = win
outcome_value = {"X": 0, "Y": 3, "Z": 6}

def main():
    input_file = open('input/day2.txt', 'r')
    file_lines = list(map(lambda l: l.strip(), input_file.readlines()))
    input_file.close()

    games_list = []
    for line in file_lines:
        games_list.append([line[0], line[2]])

    print("Answer 1: {}".format(get_hand_score_sum(games_list)))

    print("Answer 2: {}".format(get_outcome_score_sum(games_list)))

def get_hand_score_sum(games_list):
    total_score = 0
    for game in games_list:
        total_score += get_hand_score(game)
    
    return total_score

def get_hand_score(game):
    score = outcome_list.index(game[1]) + 1

    if game in win_matrix:
        score += 6
    elif game in lose_matrix:
        pass
    else:
        score += 3
    
    return score

def get_outcome_score_sum(games_list):
    total_score = 0
    for game in games_list:
        total_score += get_outcome_score(game)
    
    return total_score

def get_outcome_score(game):
    score = outcome_value[game[1]]
    if game[1] == "X":
        score += (hand_list.index(game[0]) - 1) % 3 + 1
    elif game[1] == "Y":
        score += hand_list.index(game[0]) + 1
    else:
        score += (hand_list.index(game[0]) + 1) % 3 + 1
    
    return score

main()
