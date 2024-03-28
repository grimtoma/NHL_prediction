import sys
import json
sys.path.insert(-1, '../src')
print(sys.path)
import stats_api


START_YEAR = 2022
END_YEAR = 1917
failed_games_in_row = 0

for year in range(START_YEAR, END_YEAR, -1):
    for game_num in range(1, 1313):
        game_id = stats_api.create_game_id(year, "regular", game_num)
        try:
            boxscore = stats_api.get_game_boxscore(game_id)
            linescore = stats_api.get_game_linescore(game_id)
            livefeed = stats_api.get_game_livefeed(game_id)
        except ValueError:
            failed_games_in_row += 1
            print("Failed to scrape game " + game_id)
            if failed_games_in_row > 10:
                print("Failed to scrape 10 games in a row, continuing with next year")
                failed_games_in_row = 0
                break
            else:
                continue
        with open("data/boxscore/" + game_id + ".json", "w") as f:
            json.dump(boxscore, f)
        with open("data/linescore/" + game_id + ".json", "w") as f:
            json.dump(linescore, f)
        with open("data/live/" + game_id + ".json", "w") as f:
            json.dump(livefeed, f)
        print("Scraped game " + game_id)

