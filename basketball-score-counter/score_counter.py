# Basketball Score Counter

def display_scores(scores):
    print("\n📊 Scoreboard")
    print(f"Team A: {scores['A']} | Team B: {scores['B']}\n")


def add_points(scores, team, points):
    if team in scores:
        scores[team] += points
    else:
        print("❌ Invalid team! Use 'A' or 'B'.")


def reset_game():
    print("🔄 Game has been reset!")
    return {"A": 0, "B": 0}


def main():
    scores = {"A": 0, "B": 0}

    print("🏀 Welcome to the Basketball Score Counter!")
    print("Commands:")
    print("A or B → Select Team")
    print("1 / 2 / 3 → Add Points")
    print("R → Reset Game")
    print("Q → Quit\n")

    display_scores(scores)

    while True:
        team = input("Enter team (A/B), R to reset, or Q to quit: ").upper()

        if team == "Q":
            print("\n🏁 Final Scores")
            display_scores(scores)
            print("Thank you for using the Score Counter!")
            break

        if team == "R":
            scores = reset_game()
            display_scores(scores)
            continue

        if team not in scores:
            print("❌ Invalid team! Please enter A or B.")
            continue

        try:
            points = int(input("Enter points (1, 2, or 3): "))
            if points not in (1, 2, 3):
                print("❌ Invalid points! Only 1, 2, or 3 allowed.")
                continue

            add_points(scores, team, points)
            display_scores(scores)

        except ValueError:
            print("❌ Invalid input! Please enter a number.")


if __name__ == "__main__":
    main()