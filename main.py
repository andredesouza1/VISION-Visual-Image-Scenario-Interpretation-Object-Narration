import os
from dotenv import load_dotenv
from llama_index.multi_modal_llms.gemini import GeminiMultiModal
from llama_index.multi_modal_llms.generic_utils import load_image_urls, ImageDocument

load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

temp_dir_path = os.path.abspath("./temp")
print(temp_dir_path)

file_paths = [os.path.join(temp_dir_path, file) for file in os.listdir(temp_dir_path)]
print(file_paths)

image_documents = []
for file_path in file_paths:
    # Create ImageDocument objects instead of appending raw image data
    image_documents.append(ImageDocument(image_path=file_path))

gemini_pro = GeminiMultiModal(model="models/gemini-pro-vision")

complete_response = gemini_pro.complete(
    prompt="Give me more context for this image",
    image_documents=image_documents,
)

print(complete_response)


