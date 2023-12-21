


DESCRIPTION_ACCURACY_PROMPT ="""
You are a DESCRIPTION ACCURACY grader providing a score based on the accuracy of a GENERAL DESCRIPTION compared with the contents of a IMAGE REGION DESCRIPTION ARRAY.

Output a number between 0-10 where 0 is low ACCURACY and 10 is high ACCURACY. Never elaborate.

A few additional scoring guidelines:

- Long GENERAL DESCRIPTIONS should score equally well as short GENERAL DESCRIPTIONS.

- A score should increase as the GENERAL DESCRIPTIONS provides more accurate description of the image relative to the region descriptions in the  context to  IMAGE REGION DESCRIPTION ARRAY.

- ACCURACY score should increase as the GENERAL DESCRIPTIONS provides more accurate answers considering the context of the IMAGE REGION DESCRIPTION ARRAY.

- GENERAL DESCRIPTIONS that is ACCURATE to some of the IMAGE REGION DESCRIPTION ARRAY should score of 2, 3 or 4. Higher score indicates more ACCURACY.

- GENERAL DESCRIPTIONS that is ACCURATE to most of the IMAGE REGION DESCRIPTION ARRAY should get a score of 5, 6, 7 or 8. Higher score indicates more ACCURACY.

- GENERAL DESCRIPTIONS that is ACCURATE to the entire context in the IMAGE REGION DESCRIPTION ARRAY should get a score of 9 or 10. Higher score indicates more ACCURACY.

- GENERAL DESCRIPTIONS must be accurate and precise for describing the entire IMAGE REGION DESCRIPTION ARRAY to get a score of 10.

- Answers that intentionally do not answer the question, such as 'I don't know', should also be counted as the most relevant.

- Answers that state details that are not descirbed in the IMAGE REGION DESCRIPTION ARRAY should negativly affect the score.

- Never elaborate.

IMAGE REGION DESCRIPTION ARRAY: {array}

GENERAL DESCRIPTION: {description}

ACCURACY: """



BLIND_NAVIGATION_PROMPT = """On a scale of 0 (not useful) to 10 (very useful) how useful is the following DESCRIPTION for a blind person to navigate a situation. Output a number between 0-10 where 0 is not useful and 10 as useful as possible. Never elaborate.                                                                                                                                   
 DESCRIPTION: {description}
 """