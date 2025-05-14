# score_counter.py

# Basketball Score Counter

team_a_score = 0
team_b_score = 0

def display_scores():
    print(f"\nScoreboard:\nTeam A: {team_a_score} | Team B: {team_b_score}\n")

def add_points(team, points):
    global team_a_score, team_b_score
    if team == 'A':
        team_a_score += points
    elif team == 'B':
        team_b_score += points
    else:
        print("Invalid team! Use 'A' or 'B'.")

def main():
    print("Welcome to the Basketball Score Counter!")
    display_scores()
    
    while True:
        team = input("Enter team (A/B) or Q to quit: ").upper()
        if team == 'Q':
            print("Final Scores:")
            display_scores()
            break

        try:
            points = int(input("Enter points (1, 2, or 3): "))
            if points not in [1, 2, 3]:
                print("Invalid points! Only 1, 2, or 3 allowed.")
                continue
            add_points(team, points)
            display_scores()
        except ValueError:
            print("Invalid input! Please enter a number.")

if __name__ == "__main__":
    main()
