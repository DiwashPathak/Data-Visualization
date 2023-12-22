from random import choice

class RandomWalk:
    """ A class to generate random walks"""

    def __init__(self, num_points = 5000):
        """ Initalize attributes of walk"""
        self.num_points = num_points

        # Starting walk at (0, 0)
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self, get_steps):
        """Append values to x_values and y_values"""
        
        while len(self.x_values) < self.num_points:
            # get_steps function returns x_step and y_step in a dictionary
            both_steps = get_steps()

            # Determining how much points to move
            x_step = both_steps["x_step"]
            y_step = both_steps["y_step"]

            # Next step
            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step

            # Add points to x and y values
            self.x_values.append(next_x)
            self.y_values.append(next_y)