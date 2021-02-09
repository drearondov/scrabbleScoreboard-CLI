import typer

from __future__ import print_function, unicode_literals
from pyfiglet import figlet_format
from PyInquirer import prompt

from scrabbleScoreboard.auth import login

app = typer.Typer()


@app.command()
def init():
    typer.echo("\nWelcome to")
    welcome_text = figlet_format("Scrabble Scoreboard!")
    typer.echo(welcome_text)

    question = [
        {
            'type': 'list',
            'name': 'next_step',
            'message': 'where to next?',
            'choices': ['login', 'new game'],
            'default': 'login'
        }
    ]

    answer = prompt(question)

    if answer['next_step'] == 'login':
        login()
    elif answer['next_step'] == 'new_game':
        # TODO: Create new game function.
        pass


@app.callback()
def main(verbose: bool = False):
    """
    CLI client for Scrabble Scoreboard API.
    """
    pass


if __name__ == "__main__":
    app()
