#sr_visual.py
from survery import Survey
import pygal

# Create a new  survey and take a survey
question = "Best teacher of 8D?"
survey = Survey(question)
survey.take_survery()

# Calculate frequencies of opinions
frequencies = []
for opinion in survey.type_opinions:
    frequencies.append(survey.results.count(opinion))

# Make a bar diagram to show result of survey
hist = pygal.Bar()

# Adding necessary things in chart
hist.title = f"Result of {question} with {survey.num_opinion} opinion"


# Add x_labels
hist.x_labels = []
for opinion in survey.type_opinions:
    hist.x_labels.append(opinion)

# Addig title for x and y axis
hist.x_title = "Languages"
hist.y_title = "Frequency of languages"

# Adding frequency to hist
hist.add("languages", frequencies )

# Rendering an image of information
hist.render_to_file("results.svg")