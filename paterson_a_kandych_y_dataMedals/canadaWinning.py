import csv
import numpy as np
import matplotlib.pyplot as plt

canada = []
world = []


categories = []

with open ("data/OlympicsWinter.csv") as csvfile:
    reader = csv.reader(csvfile)
    line_count = 0

    for row in reader:
        if line_count is 0:
            categories.append(row)
            line_count += 1

        elif row[4] == "CAN":
            canada.append([int(row[0]), row[2], row[5], row[6], row[7]])
        else:
            world.append([int(row[0]), row[2], row[5], row[6], row[7]])
        line_count += 1

print("total medals for canada:", len(canada))
print("rest of the world:", len(world))


print(canada[0])

print ("processed", line_count, "rows of data")

gold_1924 = []
gold_1948 = []
gold_1973 = []
gold_2002 = []
gold_2014 = []

for medal in canada:
    if medal[0] == 1924 and medal[4] == "Gold":
        gold_1924.append(medal)
    if medal[0] == 1948 and medal[4] == "Gold":
        gold_1948.append(medal)
    if medal[0] == 1973 and medal[4] == "Gold":
        gold_1973.append(medal)
    if medal[0] == 2002 and medal[4] == "Gold":
        gold_2002.append(medal)
    if medal[0] == 2014 and medal[4] == "Gold":
        gold_2014.append(medal)

print("Canada won", len(gold_1924), "gold medals in 1924")
print("Canada won", len(gold_2014), "gold medals in 2014")

skiing_2014 = []


for medal in gold_2014:
    if row[7] == "Gold":
        skiing_2014.append(medal)

print("Canada", len(skiing_2014))
print("world", len(skiing_2014))

labels = ["canada" , "world"]
values = [4, 60]


colors = ["gold", "silver"]
explode = (0.1, 0.1)

plt.pie(values, labels=labels, explode=explode, 
    colors=colors, autopct="%1.1f%%", shadow=True, startangle=140)
plt.axis("equal")

plt.legend(labels, loc=1)
plt.title("Canada & Sport in 2014")
plt.xlabel("Skinning")

plt.show()


