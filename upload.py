from datasets import load_dataset


dataset = load_dataset("csv", data_files=["data.csv"], split="train")
print(dataset)
dataset.push_to_hub("tuna2134/gigazine-label")