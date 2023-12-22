from matplotlib import pyplot
from randomwalk import RandomWalk
from rw_functions import get_steps

# Make random_walks and plot them on points
rw = RandomWalk(50_000)

while True:
    # Make new random walks and plot the points
    rw = RandomWalk()
    rw.fill_walk(get_steps)

    # Changing the size of chart
    pyplot.figure(dpi = 128, figsize = (10, 6))

    point_numbers = list(range(rw.num_points))
    pyplot.scatter(rw.x_values , rw.y_values , s = 2,edgecolor ="none", c = point_numbers, cmap = pyplot.cm.Blues)
    
    # Emphasize the first and list points
    pyplot.scatter(0, 0, c='green', edgecolors='none')
    pyplot.scatter(rw.x_values[-1], rw.y_values[-1] , edgecolor="none", c="red")
   
    # Remove the axis
    
    pyplot.gca().get_xaxis().set_visible(False)
    pyplot.gca().get_yaxis().set_visible(False)


    # Show our chart
    pyplot.show()

    # Asking to make another random_walk or not
    keep_running = input("Make another walk y/n: ")

    if keep_running == "n":
        break