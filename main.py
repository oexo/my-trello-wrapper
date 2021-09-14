import argparse
import json
import os

from trello_lib import get_trello_boards, get_trello_board

TRELLO_API_KEY = os.getenv("TRELLO_API_KEY")
TRELLO_TOKEN = os.getenv("TRELLO_TOKEN")


def parse_args():

    parser = argparse.ArgumentParser()

    parser.add_argument("-b", "--board")
    parser.add_argument("-l", "--list")

    print(parser.parse_args())


def main():

    all_boards = get_trello_boards(TRELLO_API_KEY, TRELLO_TOKEN)
    selected_board = get_trello_board('60e85c0858520246ff4c9eef', TRELLO_API_KEY, TRELLO_TOKEN)

    print(json.dumps(all_boards, sort_keys=True, indent=4, separators=(",", ": ")))
    # print(json.dumps(selected_board, sort_keys=True, indent=4, separators=(",", ": ")))


if __name__ == "__main__":
    main()

