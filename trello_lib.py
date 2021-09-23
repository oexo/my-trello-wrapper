import requests


def get_trello_boards(api_key: str, api_token: str) -> dict:

    url = "https://api.trello.com/1/members/me/boards"
    query = {
        'key': api_key,
        'token': api_token
    }
    response = requests.get(url, params=query).json()
    return response


def get_trello_board(board_id: str, api_key: str, api_token: str) -> dict:

    url = f"https://api.trello.com/1/boards/{board_id}"
    query = {
        'key': api_key,
        'token': api_token
    }
    response = requests.get(url, params=query).json()
    return response


def add_trello_board(board_name: str, api_key: str, api_token: str) -> dict:

    url = "https://api.trello.com/1/boards/"
    query = {
        'key': api_key,
        'token': api_token,
        'name': board_name
    }
    response = requests.post(url, params=query).json()
    return response

