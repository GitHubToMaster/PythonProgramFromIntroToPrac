# 从文件中读取日期，最高气温和最低气温
from datetime import datetime
from matplotlib import pyplot as plt
import csv
with open('../sitka_weather_2014.csv') as f:
    reader = csv.reader(f)
    header_row = next(reader)

    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[0], "%Y-%m-%d")
        dates.append(current_date)
        highs.append(int(row[1]))
        lows.append(int(row[3]))

fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates, highs, c='red')
plt.plot(dates, lows, c='blue')
plt.title("Daily high and low temperatures, 2014", fontsize=24)
plt.xlabel('', fontsize=16)
plt.ylabel("Temperature (F)", fontsize=16)
fig.autofmt_xdate()
plt.tick_params(axis="both", labelsize=16)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.5)  # alpha指定颜色透明度，0表示完全透明
plt.show()
