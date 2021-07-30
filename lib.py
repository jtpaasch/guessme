"""The library for our little game."""

import random
from os import system
import sys

def draw_logo():
    """Draw the logo."""
    print("")
    print("")
    print("-----------------------")
    print("  //    //   =======   ")
    print("  ||   ||   //     //  ")
    print("  ||   ||   ||     ||  ")
    print("  ||   //   ||  *  ||  ")
    print("  ||= //    ||     ||  ")
    print("     ||     ||     ||  ")
    print("     ||     //     //  ")
    print("     ||     ========   ")
    print("-----------------------")
    print("")
    print("")

def draw_score(program_data):
    """Display the current score."""
    correct_score = str(program_data["correct"])
    incorrect_score = str(program_data["incorrect"])
    print("Correct: " + correct_score + " - Incorrect: " + incorrect_score)
    print("")

def clear_screen():
    """ Clear the terminal/screen."""
    system("clear")

def draw_correct_screen(program_data):
    """Draw the 'you are correct' screen."""
    clear_screen()
    draw_logo()
    draw_score(program_data)
    print("Correcto mundo")
    user_input = input("Enter 'b' to try again or 'q' to quit: ")
    if user_input == "b":
        draw_guess_screen(program_data)
    elif user_input == "q":
        sys.exit()
    else:
        draw_correct_screen(program_data)

def draw_error_screen(program_data, msg):
    """Draw an error message on the screen."""
    clear_screen()
    draw_logo()
    draw_score(program_data)
    print(msg)
    user_input = input("Enter 'b' to try again or 'q' to quit: ")
    if user_input == "b":
        draw_guess_screen(program_data)
    elif user_input == "q":
        sys.exit()
    else:
        draw_error_screen(program_data, msg)

def draw_guess_screen(program_data):
    """Draw the 'guess a number' screen."""
    clear_screen()
    draw_logo()
    draw_score(program_data)
    print("Guess a number between 1 and 10.")
    guessed_number = input("Your guess: ")
    try:
        guessed_int = int(guessed_number)
    except ValueError:
        guessed_int = None
    if guessed_int is None:
        msg = "You must guess an integer"
        draw_error_screen(program_data, msg)
    else:
        actual_number = random.randint(1, 10)
        if guessed_int == actual_number:
            program_data["correct"] = program_data["correct"] + 1
            draw_correct_screen(program_data)
        else:
            program_data["incorrect"] = program_data["incorrect"] + 1
            msg = "You wrong. You dumb"
            draw_error_screen(program_data, msg)

