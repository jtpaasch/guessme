"""The main entry point into the program."""

import lib

def run():
    """Start up the program."""
    program_data = {"correct": 0, "incorrect": 0}
    lib.draw_guess_screen(program_data)

if __name__ == "__main__":
    run()
