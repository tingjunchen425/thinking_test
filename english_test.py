import PIL
import PIL.Image
import google.generativeai as generativeai
import dotenv
import os

dotenv.load_dotenv()
api_key = os.getenv("gemini_api_key")
model = generativeai.GenerativeModel("gemini-2.0-flash-thinking-exp")
image = PIL.Image.open("thinking_test/english/img/1.jpg")
prompt = f"""This is a English question.
            Try to read and solve the question in the image.
            Think step by step.
            Only return the answer.
            If the question is a choice question, return which answer you choice.
            The return type should be like this:
                process: I choose A because...
                Answer: A
                using time: 10s
            """
resp = model.generate_content(
    [prompt,image]
)
print(resp.text)