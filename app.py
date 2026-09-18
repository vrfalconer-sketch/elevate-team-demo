"""Simple Argolis Vertex AI App for Collaborative Git Practice."""

import os
os.environ["GOOGLE_API_USE_CLIENT_CERTIFICATE"] = "false"

from google import genai
from google.genai import types

PROJECT_ID = os.environ.get("GOOGLE_CLOUD_PROJECT", "elevate-prep-508304")
LOCATION = os.environ.get("GOOGLE_CLOUD_LOCATION", "us-central1")


def ask_gemini(prompt: str) -> str:
    """Calls Gemini 2.5 Flash with an Enterprise Security System Instruction."""
    client = genai.Client(vertexai=True, project=PROJECT_ID, location=LOCATION)
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
        config=types.GenerateContentConfig(
            system_instruction="You are an Altostrat Principal AI Security Architect. Always emphasize security guardrails.",
            temperature=0.1,
        ),
    )
    return response.text.strip()


if __name__ == "__main__":
    print(f"🛡️ Connecting to Argolis Security Engine: {PROJECT_ID} ({LOCATION})...")
    question = "Give a 1-sentence tip for a team of Customer Engineers collaborating on GitHub."
    print(f"❓ Question: {question}\n")
    answer = ask_gemini(question)
    print(f"💡 Security Architect Response:\n   {answer}")
