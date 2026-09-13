import warnings
import time

warnings.filterwarnings("ignore")

from google import genai
from google.genai import errors

client = genai.Client(api_key="AQ.Ab8RN6J7jG8KXh1t56Eu9JDZ8unqhas2fb2WC3e27awIPsRT-g")

while True:
    question = input("You: ")

    if question.lower() == "exit":
        break

    try:
        response = client.models.generate_content(
            model="gemini-3.6-flash",
            contents=question,
        )
        print("gemini:", response.text)

    except errors.APIError as e:
        print(f"\n[API Notice]: {e.message}")
        print("Waiting 2 seconds before you try again...\n")
        time.sleep(2)