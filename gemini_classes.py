
from trulens_eval.tru_custom_app import instrument

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