import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


def generate_ai_response(note):

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {
                "role": "user",
                "content": f"""
You are an AI assistant for an HCP CRM.

Analyze this doctor interaction note:

{note}

Return response in this format:

Summary:
(write short summary)

Sentiment:
(Positive / Negative / Neutral)

Follow_up:
(write recommended next action)
"""
            }
        ]
    )

    return response.choices[0].message.content
