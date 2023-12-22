import csv
from datetime import datetime
from matplotlib import pyplot as plt
#high_lows.py
filename = "deathvalley_weather.csv" 
with open(filename) as f:
    rows = csv.reader(f)
    header_column = next(rows)
         
     
    # row is list of comma separated rows
    dates , high_temps, low_temps = [], [], []
    # Getting list of rows
    for row in rows:

        try:
            # Getting dates
            date = datetime.strptime(row[2],  "%Y-%m-%d")
    
            # Append max temps and lows to list
            max = int(row[4])
            low = int(row[5])
        
        except ValueError:
            print(date, "is missing data")
        
        else:
            # Low temp and high temp & dates to list
            dates.append(date)
            high_temps.append(max)
            low_temps.append(low)
    

# Plotting the High temp and Low temp
fig = plt.figure(dpi = 128, figsize = (10, 6))
plt.plot(dates, high_temps, c = "red")
plt.plot(dates, low_temps, c = "blue")
plt.fill_between(dates, high_temps, low_temps, facecolor = "blue", alpha = 0.3)

# Formatting the chart
plt.title("Daily temperature of Sitika in 2021")
plt.xlabel("Date")
plt.ylabel("Temperature")
plt.tick_params(axis='both', colors = "gray", labelsize = 8)
fig.autofmt_xdate()

# Show
# plt.savefig("temperature1.png", bbox_inches = "tight")
plt.show()