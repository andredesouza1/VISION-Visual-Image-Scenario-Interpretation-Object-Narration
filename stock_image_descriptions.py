import google.generativeai as genai
import os
from dotenv import load_dotenv
from IPython.display import JSON
from PIL import Image
import io
from llama_index.schema import ImageDocument
from llama_index.multi_modal_llms.gemini import GeminiMultiModal
import time
import csv

load_dotenv()

GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')





images_folder = "./image_test"

# Collect image paths in the folder
image_paths = [os.path.join(images_folder, file) for file in os.listdir(images_folder) if file.endswith(('.jpg', '.jpeg', '.png'))]

# Create ImageDocument instances for each image
image_documents = [ImageDocument(image_path=image_path) for image_path in image_paths]

# Print the list of ImageDocument instances
print(len(image_documents))

def describe_images(image_documents,image_paths):
    results = []
    gemini_pro = GeminiMultiModal(model_name="models/gemini-pro-vision")
    for index, image_document in enumerate(image_documents):
        print("Starting...")
        completion = gemini_pro.complete(
            prompt="Provide a detailed description of the image.",
            image_documents=[image_document],
        )
        results.append({"image_url": image_paths[index], "description": completion.text})
        print("Images Described:", index + 1, "/", len(image_documents))
        time.sleep(2)
    return results


results = describe_images(image_documents, image_paths)


csv_file_path = "image_descriptions_1.csv"

with open(csv_file_path, mode='w', newline='', encoding='utf-8') as csv_file:
    fieldnames = ['image_url', 'description']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    # Write the header
    writer.writeheader()

    # Write the data
    for result in results:
        writer.writerow(result)



for result in results:
    print(result)







