import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

# Make a request
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
res = requests.get(url)

# Make dictionary of responce
res_dict = res.json()

# Catching repositories
repos_list = res_dict['items']

print(len(repos_list))

# Storing name and stars of repo
names , stars = [], []
for repo in repos_list:
        names.append(repo["name"])
        stars.append(repo["stargazers_count"])

# Creating visualation according to frequency = stars and names = x_labels
# my_style = LS('#333366', base_style=LCS)

my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.title_font_size = 24
my_config.label_font_size = 18
my_config.major_label_font_size = 18
my_config.truncate_label = 15
my_config.show_y_guides = False
my_config.width = 1000
chart = pygal.Bar(my_config)

chart.title = "Repositories with most starts"
chart.x_title = "Names"
chart.y_title = "Stars"
chart.x_labels = names

chart.add("repos", stars)
chart.render_to_file("repos.svg")