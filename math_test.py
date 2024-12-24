import PIL.Image
import google.generativeai as generativeai
import PIL
from PIL import Image, ImageDraw, ImageFont
from dotenv import load_dotenv
import os
import time

load_dotenv()
api_key = os.getenv("gemini_api_key")

model = generativeai.GenerativeModel("gemini-2.0-flash-thinking-exp")
image = PIL.Image.open("thinking_test/math/junior_high/25.jpg")
prompt = f"""This is a math question.
            Try to read and solve the question in the image.
            Only return the answer.
            Think step by step.
            If the question is a choice question, return which answer you choice.
            The return type should be like this:
                process: 1+1=2
                Answer: 2
                using time: 10s
            """
resp = model.generate_content(
    [prompt,image]
)
print(resp.text)