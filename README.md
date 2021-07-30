# Guess Me

A simple demo/game in Python.

To run this code, go to this folder in your terminal, then execute:

```
python3 -m main
```

Or:

```
python3 main.py
```

If you want to play around with the functions in the REPL, go to this folder
in your terminal, then execute:

```
python3
```

Then import the library:

```
>>> import lib
```

You can then call functions, for example:

```
>>> data = {"correct": 0, "incorrect": 10}
>>> lib.draw_correct_screen(data)
```


## Gameplan/User story

```

  Start up:
  - Set the scores (a tally of correct and incorrect guesses) to zero
  - Go to guess screen

  Guess screen (is given SCORES to display)
  +----------------
  |
  |  <LOGO GOES HERE>
  |
  |  <SCORES DISPLAYED HERE>
  |
  |  Guess a number between 1 and 10
  |  Your guess: _
  |
  +--------------------
  LOGIC:
  - Get a random integer between 1 and 10 and assign it to actual_number 
  - Collect user input
  - Try to cast the user input to an integer
    - If it works, assign it to the guessed_number
    - If you get an error, set the guessed_number to None
  - If the guessed number is None
    - This means the user entered text that's not an integer
    - call draw_error_screen with an appropriate message
  - else if the guessed number equals the actual number:
    - update the scores
    - call draw_correct_screen() with the scores
  - else
    - update the scores
    - call draw_error_screen() with the scores and an appropriate message

  Error screen (is given SCORES to display, and an error MESSAGE to display)
  +------------------
  |
  |  <MESSAGE>
  |
  |  <SCORES DISPLAYED HERE>
  |
  |  Press b to try again or q to quit: _
  |
  +------------------
  LOGIC:
  - When 'b' is pressed, call draw_guess_screen() with scores
  - When 'q' is pressed, exit the program
  - Anything else, call draw_error_screen again with same scores and message

  Correct screen (is given SCORES to display)
  +-----------------
  |
  |  Correct! 
  |
  |  <SCORES DISPLAYED HERE>
  |
  |  Press b to try again or q to quit: _
  |
  +----------------
  LOGIC:
  - When 'b' is pressed, call draw_guess_screen() with scores
  - When 'q' is pressed, exit the program
  - Anything else, call draw_error_screen again with same scores and message

```

## Files

* lib.py:
  * `draw_guess_screen()`:
    * Clears the screen
    * Draws the logo
    * Asks the user to guess a number between 1 and 10
    * Does the LOGIC described above
  * `draw_error_screen(msg)`:
    * Clears the screen
    * Draws the logo
    * Displays the provided `msg`
    * Does the error screen LOGIC described above
  * `draw_correct_screen()`:
    * Clears the screen
    * Draws the logo
    * Displays a "you are correct" message
    * Does the correct screen LOGIC described above

* main.py:
  * `run()`:
    * sets up any data that we have to track (none for now)
    * calls `draw_guess_screen()`
  * if __name__ == "__main__":
    * Calls `run()`
