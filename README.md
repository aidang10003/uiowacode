### Computational Thinking Final Project - 5/3/2020

## University of Iowa

A word guessing game where you compete against the computer to guess a three, four, or five letter word before the computer.
We made this game in 2020, but exxentially it's the same thing as Wordle.

## Running the code

1.  Clone this repository to local computer

2.  If you already have a ./venv folder skip this step

    Create a new virtual environment

    - Windows: `python -m venv ./venv`
    - Mac: `python3 -m venv ./venv`

3.  Activate the new virtual environment

    - Windows:
      `.\venv\Scripts\activate`
    - Mac:
      `source ./venv/bin/activate`

4.  Install the dependencies

        `pip install -r requirements.txt`

5.  Run the webscrape document, this will take 5-10 minutes, but is essential to generating the game data.

    - For a quick download you can alter the funtion in the webscrape denoted by the comments
      `py .\webscrape_function.py`

6.  Next run the main game function to play!

    `py .\main_game.py`
