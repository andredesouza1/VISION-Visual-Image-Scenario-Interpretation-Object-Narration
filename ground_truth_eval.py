import set_tru
from trulens_eval.tru_custom_app import instrument

from llama_index.multi_modal_llms.gemini import GeminiMultiModal

from llama_index.multi_modal_llms.generic_utils import (
    load_image_urls,
)
import json
from dotenv import load_dotenv
import os
from trulens_eval import TruCustomApp

load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

with open("subset_dataset.json") as f:
    subset_dataset = json.load(f)

from trulens_eval import Feedback
from trulens_eval.feedback import GroundTruthAgreement

gemini_pro = GeminiMultiModal(model_name="models/gemini-pro-vision")

class Gemini:
    @instrument
    def complete(self, prompt, image_documents):
        completion = gemini_pro.complete(
            prompt=prompt,
            image_documents=image_documents,
        )
        return completion



def evaluate_ground_truth(subset_dataset):
    # set golden set and image documents
    counter = 0
    set_of_sets = []
    image_urls = []
    for i in range(len(subset_dataset["qas"])):
        if subset_dataset["qas"][i] != []:
            image_urls.append([subset_dataset["url"][i]])
            counter = counter + 1
            for j in range(len(subset_dataset["qas"][i])):
                set_of_sets.append({"query": subset_dataset["qas"][i][j]['question'], "response": subset_dataset["qas"][i][j]['answer']})
                print("j:", j)
        print("i:", i)
    print("counter:", counter)
    # evaluate ground truth
    gemini = Gemini()
    for i in range(0, counter):
        golden_set = []
        for j in range(len(subset_dataset["qas"][i])):
            golden_set.append(set_of_sets.pop(0))
        
        print("golden set:", golden_set)
        print(len(golden_set))
        print(len(subset_dataset["qas"][i]))

        f_groundtruth = Feedback(GroundTruthAgreement(golden_set).agreement_measure, name = "Ground Truth").on_input_output()
        
    
    
    
        tru_app = TruCustomApp(gemini, app_id = f'Ground_Truth_Eval_Image_{i}', feedbacks = [f_groundtruth])
    
         
        with tru_app as recording:
            for a in range(len(subset_dataset["qas"][i])):
                try: 
                    if golden_set != []:
                        image_documents = load_image_urls(image_urls[i])
                        gemini.complete(prompt = golden_set[a]["query"], image_documents=image_documents)
                        print("a:", a)
                        if a > 60:
                            break
                except Exception as e:
                    # Handle the exception (optional)
                    print(f"An error occurred in iteration {a}: {e}")  
            print("Loop completed successfully.")     

    set_tru.tru.run_dashboard()


if __name__ == "__main__":
    evaluate_ground_truth(subset_dataset)
        


            
        
    
