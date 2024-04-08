#!/usr/bin/env python3
from brain_games import cli
from brain_games import is_even_game


def main():
    print('Welcome to the Brain Games!')
    name = cli.welcome_user()
    is_even_game.game(user_name=name)


if __name__ == '__main__':
    main()
