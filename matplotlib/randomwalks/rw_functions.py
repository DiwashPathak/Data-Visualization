# rw_functions.py
from random import choice

def get_steps():

    # Determine direction
    x_direction = choice([1 , -1])
    y_direction  = choice([1, -1])

    # Determine distance
    x_distance = choice([1, 2, 3, 4])
    y_distance = choice([1, 2, 3, 4])

    # Set how much steps to move
    x_step = x_direction * x_distance
    y_step = y_direction * y_distance

    # Storing x_step and y_step in list
    both_values = {
        "x_step": x_step,
        "y_step": y_step
    }
    # Returning both values
    return both_values