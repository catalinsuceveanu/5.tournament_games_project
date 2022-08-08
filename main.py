import processor


def main():
    teams = {}
    no_of_teams = get_the_correct_input_for_no_of_teams()
    for team_no in range(no_of_teams):
        teams[get_the_correct_input_for_team_name(team_no, teams)] = None
    no_of_games_played_during_season = (
        get_the_correct_input_for_no_of_games_played_during_season(no_of_teams)
    )
    for team in teams:
        teams[team] = get_the_correct_input_for_no_of_wins_per_team(
            team, no_of_games_played_during_season
        )
    games_to_be_played = []


def get_the_correct_input_for_no_of_teams():
    correct_input = False
    current_input = None
    while correct_input == False:
        current_input = int(input("Enter the number of teams in the tournament: "))
        if current_input % 2 == 0 and current_input > 0:
            correct_input = True
        else:
            print(
                f">> {current_input} << is invalid. Please insert an evan positive number."
            )
    return current_input


def get_the_correct_input_for_team_name(team_no, teams):
    correct_input = False
    current_input = None
    while correct_input == False:
        current_input = input(f"Enter the name of team {team_no + 1}: ")
        if len(current_input) >= 2 and current_input not in teams:
            correct_input = True
        elif current_input in teams:
            print(f"Team {current_input} is already on the roaster")
        else:
            print(
                f">> {current_input} << is invalid. Please insert at name at least 2 letters long"
            )
    return current_input


def get_the_correct_input_for_no_of_games_played_during_season(no_of_teams):
    correct_input = False
    current_input = None
    while correct_input == False:
        current_input = int(input(f"Enter the number of games played by each team: "))
        if current_input >= no_of_teams - 1:
            correct_input = True
        else:
            print(
                f">> {current_input} << is invalid. Each team plays each other at least once in the regular season, try again."
            )
    return current_input


def get_the_correct_input_for_no_of_wins_per_team(
    team, no_of_games_played_during_season
):
    correct_input = False
    current_input = None
    while correct_input == False:
        current_input = int(
            input(f"Enter the number of wins {team} had during the season: ")
        )
        if current_input <= no_of_games_played_during_season:
            correct_input = True
        else:
            print(
                f"The maximum number of wins is {no_of_games_played_during_season}, try again."
            )
    return current_input


if __name__ == "__main__":
    main()
