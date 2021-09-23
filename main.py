#!/usr/bin/python3

import argparse
import json
import os

from trello_lib import get_trello_boards, get_trello_board, add_trello_board

TRELLO_API_KEY = os.getenv("TRELLO_API_KEY")
TRELLO_TOKEN = os.getenv("TRELLO_TOKEN")


def parse_args():

    parser = argparse.ArgumentParser()

    parser.add_argument("-a", "--add", action="store_true")
    parser.add_argument("-g", "--get", action="store_true")
    parser.add_argument("-b", "--board")
    parser.add_argument("-l", "--list")

    return parser.parse_args()


def is_board_exists(board_name: str, all_boards: dict) -> bool:
    for board in all_boards:
        if board["name"] == board_name:
            return True
    return False


def main():

    args = parse_args()

    all_boards = get_trello_boards(TRELLO_API_KEY, TRELLO_TOKEN)

    # print(json.dumps(all_boards, sort_keys=True, indent=4, separators=(",", ": ")))

    if args.get:
        if args.board:
            board_id = ""
            for board in all_boards:
                if board["name"] == args.board:
                    board_id = board["id"]
            selected_board = get_trello_board(board_id, TRELLO_API_KEY, TRELLO_TOKEN)
            print(json.dumps(selected_board, sort_keys=True, indent=4, separators=(",", ": ")))
        else:
            for board in all_boards:
                print(board["name"], board["id"])
    elif args.add:
        if args.board:
            if is_board_exists(args.board, all_boards):
                print(f"The board with the name {args.board} is already exists")
            else:
                new_board = add_trello_board(args.board, TRELLO_API_KEY, TRELLO_TOKEN)
                print(f"Created the board with name: {new_board['name']} and id: {new_board['id']} ")


if __name__ == "__main__":
    main()

