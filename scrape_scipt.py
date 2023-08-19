import stats_api
import json

for year in range(2022, 2023):
    for game_num in range(1, 1313):
        game_id = stats_api.create_game_id(year, "regular", game_num)
        try:
            boxscore = stats_api.get_game_boxscore(game_id)
            linescore = stats_api.get_game_linescore(game_id)
            livefeed = stats_api.get_game_livefeed(game_id)
        except ValueError:
            print("Failed to scrape game " + game_id)
            continue
        with open("data/boxscore/" + game_id + ".json", "w") as f:
            json.dump(boxscore, f)
        with open("data/linescore/" + game_id + ".json", "w") as f:
            json.dump(linescore, f)
        with open("data/live/" + game_id + ".json", "w") as f:
            json.dump(livefeed, f)
        print("Scraped game " + game_id)

