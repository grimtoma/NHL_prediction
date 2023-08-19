import requests

BASE_URL = "https://statsapi.web.nhl.com/api/v1/"



def create_game_id(year: int, type: str, game_num: int) -> str:
    """Creates a game_id from the year, type, and game_num
    The first 4 digits identify the season of the game (ie. 2017 for the 2017-2018 season).
    The next 2 digits give the type of game, where 01 = preseason, 02 = regular season, 03 = playoffs, 04 = all-star.
    The final 4 digits identify the specific game number. For regular season and preseason games, this ranges from 0001 to the number of games played.
    (1271 for seasons with 31 teams (2017 and onwards) and 1230 for seasons with 30 teams).
    For playoff games, the 2nd digit of the specific number gives the round of the playoffs, the 3rd digit specifies the matchup, and the 4th digit specifies the game (out of 7).
    """
    if type == "preseason":
        type = "01"
    elif type == "regular":
        type = "02"
    elif type == "playoffs":
        type = "03"
    elif type == "all-star":
        type = "04"
    else:
        raise ValueError("Invalid game type")
    return str(year) + type + str(game_num).zfill(4)


def get_game_boxscore(game_id: str) -> dict:
    """Returns the boxscore (medium detail) for a given game"""
    url = BASE_URL + "game/" + game_id + "/boxscore"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        raise ValueError("Invalid game_id")


def get_game_linescore(game_id: str) -> dict:
    """Returns the linescore (low detail) for a given game"""
    url = BASE_URL + "game/" + game_id + "/linescore"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        raise ValueError("Invalid game_id")


def get_game_livefeed(game_id: str) -> dict:
    """Returns the livefeed (high detail) for a given game"""
    url = BASE_URL + "game/" + game_id + "/feed/live"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        raise ValueError("Invalid game_id")
