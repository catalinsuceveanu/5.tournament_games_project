import input_processor as p
from plays_generator import games_generator as gg


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
    games_to_be_played = gg.generate_games(teams)
    print_games(games_to_be_played)


def print_games(games_to_be_played):
    for game in games_to_be_played:
        print(f"Home: {game[0]} VS Away: {game[1]}")


if __name__ == "__main__":
    main()
