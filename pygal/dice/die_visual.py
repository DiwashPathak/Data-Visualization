import pygal
from die import Die


# Creating D6
die_1 = Die()
die_2 = Die(10)

# Storing results in a list
results = []

for roll_num in range(50_000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

# Analyze the results.
frequencies = []
max_sides = die_1.num_sides + die_2.num_sides
for value in range(1, max_sides + 1):
    frequency = results.count(value)
    frequencies.append(frequency)
    
# Visualize the results
hist = pygal.Bar()

hist.title = f"Results of rolling two dice 50000 times {die_1.num_sides + die_2.num_sides}"
hist.x_labels = []

# Adding x_lables
for side in range(1, max_sides + 1):
    hist.x_labels.append(str(side))

hist.x_title = "Result"
hist.y_title = "Frequency of results"

hist.add("D6 + D6", frequencies)
hist.render_to_file("die_visual.svg")