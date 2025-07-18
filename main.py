import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def obtener_planing():
    prompt = "Tengo 3 montadores disponibles y 5 faenas. ¿Cómo las asignarías esta semana?"

    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    print(response.choices[0].message.content)

if __name__ == "__main__":
    obtener_planing()
