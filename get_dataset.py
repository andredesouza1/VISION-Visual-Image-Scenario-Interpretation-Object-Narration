import json
from datasets import load_dataset, Dataset

# Load the dataset
dataset = load_dataset("visual_genome", "relationships_v1.0.0")
total_number = 500
# Load a smaller subset, e.g., first 1000 samples
subset_dataset = dataset["train"].select([i for i in range(total_number)])

# Define your filtering logic and create filtered_data


# Convert the modified dataset to a dictionary
subset_dict = subset_dataset.to_dict()

# Save the dictionary as a JSON file
with open("subset_dataset_answers.json", "w", encoding="utf-8") as json_file:
    json.dump(subset_dict, json_file, ensure_ascii=False, indent=2)
