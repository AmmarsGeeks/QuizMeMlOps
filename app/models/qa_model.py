from openai import OpenAI
from dotenv import load_dotenv
import os

class QAModel:
    def __init__(self):
        load_dotenv()
        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    
    def generate_answer(self, context: str, question: str):
        response = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": f"Answer this question based on the context: {context}"},
                {"role": "user", "content": question}
            ]
        )
        return response.choices[0].message.content