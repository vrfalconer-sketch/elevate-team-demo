"""Simple Argolis Vertex AI App for Collaborative Git Practice.

Run with:
    python app.py
"""

import os
os.environ["GOOGLE_API_USE_CLIENT_CERTIFICATE"] = "false"

from google import genai

PROJECT_ID = os.environ.get("GOOGLE_CLOUD_PROJECT", "elevate-prep-508304")
LOCATION = os.environ.get("GOOGLE_CLOUD_LOCATION", "us-central1")


def ask_gemini(prompt: str) -> str:
    """Calls Gemini 2.5 Flash on Google Cloud Vertex AI."""
    client = genai.Client(vertexai=True, project=PROJECT_ID, location=LOCATION)
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
    )
    return response.text.strip()


if __name__ == "__main__":
    print(f"🚀 Connecting to Argolis Project: {PROJECT_ID} ({LOCATION})...")
    question = "Give a 1-sentence tip for a team of Customer Engineers collaborating on GitHub."
    print(f"❓ Question: {question}\n")
    answer = ask_gemini(question)
    print(f"💡 Gemini Response:\n   {answer}")
