import google.generativeai as genai
from sys import stdin
from dotenv import load_dotenv
import os

#Load envoirnment variable from .enov
load_dotenv()

#Configure Gemini API with the API key
genai.configure(api_key=os.environ["GEMINI_API_KEY"])

#Initialize the Gemini model
model = genai.GenerativeModel(model_name= "gemini-2.0-flash")

#Main chat loop
while True:

    #Get the user input from terminal
    user_input = input("\nEnter Your Question (or 'quit' to exit):")

    #Check if user wants to quit
    if user_input.lower() == 'quit':
        print("Thanks for chating! GoodBy")
        break
   
   #generate response using user's input
    response = model.generate_content(user_input)

    #Print the Res
    print("\n\response", response.text)

