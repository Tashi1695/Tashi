#########################
#####
#Tashi Dorji
#BE Electrical Engg. 1year
#02230082
######################
########
def read_input(input_file):
    with open('input_file', 'r') as file:


def get_result(my_play, opponent_play):
    if my_play == opponent_play:
        return 'y'  # Draw
    elif my_play == 'A' and opponent_play == 'B':
        return 'X'  # Lose
    elif my_play == 'B' and opponent_play == 'C':
        return 'X'  # Lose
    elif my_play == 'C' and opponent_play == 'A':
        return 'X'  # Lose
    else:
        return 'Z'  # Win

# Input data (opponent's play and expected result)
rounds = [
    ('A', 'X'),
    ('B', 'Z'),
    ('C', 'y'),
    ('B', 'X'),
    ('A', 'y')
]

for opponent_play, expected_result in rounds:
    if expected_result == 'y':
        my_play = opponent_play  # Play whatever the opponent played
    elif expected_result == 'X':
        if opponent_play == 'A':
            my_play = 'B'  # Beat rock with paper
        elif opponent_play == 'B':
            my_play = 'C'  # Beat paper with scissors
        else:
            my_play = 'A'  # Beat scissors with rock
    else:
        if opponent_play == 'A':
            my_play = 'C'  # Lose to rock with scissors
        elif opponent_play == 'B':
            my_play = 'A'  # Lose to paper with rock
        else:
            my_play = 'B'  # Lose to scissors with paper
    
    print(f"To {expected_result}, play {my_play}")