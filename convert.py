import csv
import orjson


with open("data.json", "r") as f:
    data = orjson.loads(f.read())["contents"]


labels = []
titles = []


with open("data.csv", "w") as f:
    writer = csv.DictWriter(f, ["title", "label"])
    writer.writeheader()
    for d in data:
        if d["label"] not in labels:
            labels.append(d["label"])
        d["label"] = labels.index(d["label"])
        if d["title"] not in titles:
            titles.append(d["title"])
        else:
            continue
        writer.writerow(d)

print(labels)