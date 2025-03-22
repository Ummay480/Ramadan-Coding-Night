import os
import chainlit as cl
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get API key from .env file
gemini_api_key = os.getenv("GEMINI_API_KEY")

# Configure Gemini API
genai.configure(api_key=gemini_api_key)

# Initialize Gemini model
model = genai.GenerativeModel(model_name="gemini-2.0-flash")


@cl.on_chat_start
async def handle_chat_start():
    """Handles the start of a chat session."""
    await cl.send_message("Hello! How can I help you today?")  # ✅ Fixed


@cl.on_message
async def handle_message(message: cl.Message):
    """Handles incoming messages from the user."""
    prompt = message.content

    # Generate AI response
    response = model.generate_content(prompt)

    # Extract text from response
    response_text = response.text if hasattr(response, "text") else ""

    await cl.send_message(response_text)  # ✅ Fixed
