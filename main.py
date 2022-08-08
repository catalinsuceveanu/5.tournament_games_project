teams = {}


def main():

    no_of_teams_in_tournament = get_the_correct_input(x="no_of_teams")
    for team in range(no_of_teams_in_tournament):
        teams[get_the_correct_input("team_name", team + 1)] = None
    print(teams)


def get_the_correct_input(x, no=0):
    correct_input = False
    current_input = None
    if x == "no_of_teams":
        while correct_input == False:
            current_input = int(input("Enter the number of teams in the tournament: "))
            if current_input % 2 == 0 and current_input > 0:
                correct_input = True
            else:
                print(
                    f">> {current_input} << is invalid. Please insert an evan positive number."
                )
        return current_input

    elif x == "team_name":
        while correct_input == False:
            current_input = input(f"Enter the name of team {no}: ")
            if len(current_input) >= 2 and current_input not in teams:
                correct_input = True
            elif current_input in teams:
                print(f"Team {current_input} is already on the roaster")
            else:
                print(
                    f">> {current_input} << is invalid. Please insert at name at least 2 letters long"
                )
        return current_input
    pass


if __name__ == "__main__":
    main()
