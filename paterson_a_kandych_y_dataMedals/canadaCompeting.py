import csv
import numpy as np
import matplotlib.pyplot as plt

men = []
women = []


categories = []

with open ("data/OlympicsWinter.csv") as csvfile:
    reader = csv.reader(csvfile)
    line_count = 0

    for row in reader:
        if line_count is 0:
            categories.append(row)
            line_count += 1
        else:
            if row[5] == "Men":
                men.append(row[5])
            elif row[5] == "Women":
                women.append(row[5])
            line_count += 1

print("processed", line_count, "rows of data")
print("men:", len(men))
print("women:", len(women))


pct_men = len(men) / line_count *100
pct_women = len(women) / line_count *100

labels = ["Men", "Women"]
values = [3944, 1826]
sizes = [pct_men, pct_women]
colors = ["#87CEFA"]

amount = np.arange(len(labels))

plt.bar(amount, values, color= "#87CEFA")




plt.xticks(amount, labels)
plt.yticks(values)
plt.title("Amount of Competing Women to Men in Canada")


plt.show()
