#!/usr/bin/env python3
from brain_games import cli
from brain_games.games import prime_game


def main():
    print('Welcome to the Brain Games!')
    name = cli.welcome_user()
    prime_game.game(user_name=name)


if __name__ == '__main__':
    main()
