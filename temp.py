
# Now import the module
from prompts import description_prompts
from gemini_classes import Vision_Search

# Define the 'item' variable first
item = "door"

# Use the 'item' variable in the formatted string
hello = description_prompts.visually_impaired_search_prompt.format(item=item)

print(hello)


print(Vision_Search.describe(Vision_Search.search(description_prompts.visually_impaired_search_prompt,"video_frames", "Shopping cart")))