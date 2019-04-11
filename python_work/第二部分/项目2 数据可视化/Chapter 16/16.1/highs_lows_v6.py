from datetime import datetime
from matplotlib import pyplot as plt
import csv
with open('../sitka_weather_2014.csv') as f:
    reader = csv.reader(f)
    header_row = next(reader)

    dates, temperatures = [], []
    for row in reader:
        current_date = datetime.strptime(row[0], "%Y-%m-%d")
        dates.append(current_date)
        temperatures.append(int(row[1]))

fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates, temperatures, c='red')
plt.title("Daily high temperatures, 2014", fontsize=24)
plt.xlabel('', fontsize=16)
plt.ylabel("Temperature (F)", fontsize=16)
fig.autofmt_xdate()
plt.tick_params(axis="both", labelsize=16)
plt.show()
