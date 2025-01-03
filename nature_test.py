import PIL.Image
import google.generativeai as generativeai
import PIL
from dotenv import load_dotenv
import os
import time

load_dotenv()
api_key = os.getenv("gemini_api_key")

model = generativeai.GenerativeModel("gemini-2.0-flash-thinking-exp")
image = PIL.Image.open("thinking_test/nature/junior_high/img/50.jpg")
prompt = f"""This is a Nature Science question.
            Try to read and solve the question in the image.
            Think step by step.
            If the question is a choice question, return which answer you choice.
            Try to check  the process of your thinking.
            Try to make the answer as correct as possible.
            The return type should be like this:
                process: I choose A because...
                Answer: A
                using time: 10s
            """
resp = model.generate_content(
    [prompt,image]
)
print(resp.text)