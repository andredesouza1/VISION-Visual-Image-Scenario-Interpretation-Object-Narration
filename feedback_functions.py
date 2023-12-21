import prompts.feedback_prompts as feedback_prompts
from trulens_eval import Provider, Feedback, Select, Tru

#Example of a feedback function for the Gemini provider

load_image_urls = "placeholder"
def gemini_pro():
    return "placeholder"


class Gemini_Provider(Provider):
    def city_rating(self, image_url) -> float:
        image_documents = load_image_urls([image_url])
        city_score = float(gemini_pro.complete(prompt = "Is the image of a city? Respond with the float likelihood from 0.0 (not city) to 1.0 (city).",
        image_documents=image_documents).text)
        return city_score
    

class StandAlone(Provider):
    def custom_feedback(self, my_text_field: str) -> float:
        """
        A dummy function of text inputs to float outputs.

        Parameters:
            my_text_field (str): Text to evaluate.

        Returns:
            float: square length of the text
        """
        return 1.0 / (1.0 + len(my_text_field) * len(my_text_field))
    


class Desciption_Similarity(Provider):
    def description_similarity_score(self, image_url) -> float:
        image_documents = load_image_urls([image_url])
        description_score = float(gemini_pro.complete(prompt = "Is the image of a city? Respond with the float likelihood from 0.0 (not city) to 1.0 (city).",
        image_documents=image_documents).text)
        return description_score