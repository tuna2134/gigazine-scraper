import csv
import json


with open("data.json", "r") as f:
    data = json.load(f)["contents"]


with open("data.csv", "w") as f:
    writer = csv.DictWriter(f, ["title", "label"])
    writer.writeheader()
    for d in data:
        writer.writerow(d)