import google.generativeai as genai
import os
from dotenv import load_dotenv


load_dotenv()

# Get the API key
API_KEY = os.getenv("GOOGLE_API_KEY")

if not API_KEY:
    raise ValueError("GOOGLE_API_KEY not found in environment variables! Make sure .env exists.")

genai.configure(api_key=API_KEY)


model = genai.GenerativeModel("gemini-flash-latest")

def ask_gemini(prompt: str) -> str:
    """Send prompt to Gemini and return response text."""
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error contacting Gemini API: {str(e)}"
