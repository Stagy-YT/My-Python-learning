def get_player_scores():
    player1 = float(input("Enter your score here: "))
    player2 = float(input("Enter your score here: "))
    player3 = float(input("Enter your score here: "))
    return player1, player2, player3

def calculate_total(p1, p2, p3):
    total = p1 + p2 + p3
    return total

def apply_bonus(total_player_score):
    team_bonus = total_player_score * float(input(
        r"Apply the bonus to your teams score, exp. 1.20 = 20% increase: "))
    return team_bonus

def determine_rank(bonus):
    if bonus < 100:
        rank = 4
    elif bonus <= 199 and bonus >= 100:
        rank = 3
    elif bonus <=299 and bonus >= 200:
        rank = 2
    elif bonus >= 300:
        rank = 1
    return rank

def evaluation(rank, bonus):
    if rank == 1:
        print(f"Your score is Diamond, and your combined score is {bonus}")
    elif rank == 2:
        print(f"Your score is Gold, and your combined score is {bonus}")
    elif rank == 3:
        print(f"Your score is Silver, and your combined score is {bonus}")
    elif rank == 4:
        print(f"Your score is Bronze, and your combined score is {bonus}")


p1, p2, p3 = get_player_scores()
total_player_score = calculate_total(p1, p2, p3)
bonus = apply_bonus(total_player_score)
rank = determine_rank(bonus)
evaluation(rank, bonus)
