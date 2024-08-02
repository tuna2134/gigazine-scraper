import csv
import json


with open("data.json", "r") as f:
    data = json.load(f)["contents"]


labels = []


with open("data.csv", "w") as f:
    writer = csv.DictWriter(f, ["title", "label"])
    writer.writeheader()
    for d in data:
        if d["label"] not in labels:
            labels.append(d["label"])
        d["label"] = labels.index(d["label"])
        writer.writerow(d)

print(labels)