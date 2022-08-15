import input_processor as p


def main():
    teams = {}
    no_of_teams = p.get_the_correct_input_for_no_of_teams()
    for team_no in range(no_of_teams):
        teams[p.get_the_correct_input_for_team_name(team_no, teams)] = None
    no_of_games_played_during_season = (
        p.get_the_correct_input_for_no_of_games_played_during_season(no_of_teams)
    )
    for team in teams:
        teams[team] = p.get_the_correct_input_for_no_of_wins_per_team(
            team, no_of_games_played_during_season
        )
    games_to_be_played = generate_games(teams)
    print_games(games_to_be_played)


def generate_games(teams):
    lists_of_games = []
    list_of_teams = []
    for team in teams:
        list_of_teams.append([team, teams[team]])
    list_of_teams.sort(key=lambda x: x[1])

    left_pointer = 0
    right_pointer = int(len(teams) - 1)

    while left_pointer < right_pointer:
        lists_of_games.append(
            [list_of_teams[left_pointer][0], list_of_teams[right_pointer][0]]
        )
        left_pointer += 1
        right_pointer -= 1
    return lists_of_games


def print_games(games_to_be_played):
    for game in games_to_be_played:
        print(f"Home: {game[0]} VS Away: {game[1]}")


if __name__ == "__main__":
    main()
