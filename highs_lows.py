import csv
from matplotlib import pyplot as plt
from datetime import datetime

filename = 'sitka_weather_07-2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    dates, highs = [], []
    for row in reader:
        dates.append(datetime.strptime(row[2], "%Y-%m-%d"))
        highs.append(int(row[5]))

# Нанесение на диаграмму
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates, highs, c='red')

# Форматирование диаграммы
plt.title("Where date", fontsize = 24)
plt.xlabel('', fontsize = 16)
fig.autofmt_xdate()
plt.ylabel('T (F)', fontsize = 16)
plt.tick_params(axis='both', which='major', labelsize = 16)

plt.show()
