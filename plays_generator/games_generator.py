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
