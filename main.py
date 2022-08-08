def main():
    teams = []
    no_of_teams_in_tournament = get_the_correct_input(x="no_of_teams")
    for team in range(no_of_teams_in_tournament):
        teams.append(get_the_correct_input(x="team_name"))


def get_the_correct_input(x):
    if x == "no_of_teams":
        correct_input = False
        current_input = 0
        while not correct_input:
            current_input = int(input("Enter the number of teams in the tournament: "))
            if current_input % 2 == 0 and current_input > 0:
                correct_input = True
            else:
                print(
                    f">> {current_input} << is invalid. Please insert an evan positive number."
                )
        return current_input


if __name__ == "__main__":
    main()
