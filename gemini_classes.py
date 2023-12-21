
from trulens_eval.tru_custom_app import instrument
from llama_index.multi_modal_llms.generic_utils import ImageDocument
from llama_index.multi_modal_llms.gemini import GeminiMultiModal



gemini_pro = GeminiMultiModal(model_name="models/gemini-pro-vision")



# create a custom class to instrument
class Gemini:
    @instrument
    def complete(self, prompt, image_documents):
        completion = gemini_pro.complete(
            prompt=prompt,
            image_documents=image_documents,
        )
        return completion
    
# VISION SEARCH
class Vision_Search:
    def search(self, prompt, image_path):
        image_documents = []
        for file_path in image_path:
            # Create ImageDocument objects instead of appending raw image data
            image_documents.append(ImageDocument(image_path=file_path)) 
        
        for i in range(len(image_documents))
            completion = gemini_pro.complete(
                prompt=prompt,
                image_documents=image_documents[i],
            )
            return completion