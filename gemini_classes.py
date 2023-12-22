
from trulens_eval.tru_custom_app import instrument
from llama_index.multi_modal_llms.generic_utils import ImageDocument
from llama_index.multi_modal_llms.gemini import GeminiMultiModal
from llama_index.llms.gemini import Gemini 
import set_api_key
import os
from prompts import description_prompts



gemini_pro_vision = GeminiMultiModal(model_name="models/gemini-pro-vision")
gemini_pro = GeminiMultiModal(model_name="models/gemini-pro")



# create a custom class to instrument
class Gemini:
    @instrument
    def complete(self, prompt, image_documents):
        completion = gemini_pro_vision.complete(
            prompt=prompt,
            image_documents=image_documents,
        )
        return completion
    
class Gemini_Pro:
    @instrument
    def complete(prompt):
        completion = gemini_pro.complete(
            prompt=prompt,
        )
        return completion
    
# VISION SEARCH
class Vision_Search:
    def search (prompt, image_path, item):
        
        image_documents = []
        counter = 0

        file_paths = [os.path.join(image_path, file) for file in os.listdir(image_path)]
        # print(file_paths)
    
        for file_path in file_paths:
            # Create ImageDocument objects instead of appending raw image data
            image_documents.append(ImageDocument(image_path=file_path)) 
        
        for i in range(len(image_documents)):
            print(counter)
            image = []
            image.append(image_documents[i])
            print(image)
            searching = gemini_pro.complete(
                prompt=prompt.format(item=item),
                image_documents=image,
            )
            # print(searching.text)
            if "yes" in searching.text.lower():
                # print("found")
                counter = counter + 1
            if "no" in searching.text.lower():
                if counter > 0:
                    counter = counter - 1
            if counter >= 2:
                return f"{item} found nearby", image, True, item
        return f"{item} not found nearby", image, False, item  


    def describe(search_function):
        message, image_documents, found, item = search_function[0], search_function[1], search_function[2], search_function[3]
        print(message)
        if found == True:
            description = gemini_pro.complete(
                prompt=description_prompts.visually_impaired_navigation_prompt.format(item=item),
                image_documents=image_documents,
            )
            return description.text, found, image_documents
        
         


        