import webbrowser
import pyttsx3
import google.generativeai as genai
import os
from apps import applications

# --- Configuration ---
# IMPORTANT: Replace 'YOUR_GEMINI_API_KEY' with your actual API key.
# It's highly recommended to use environment variables for your API key
# to keep it secure and avoid hardcoding it directly in your script.
# Example: export GEMINI_API_KEY='YOUR_API_KEY' in your terminal
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")
print(GEMINI_API_KEY)

if not GEMINI_API_KEY:
  raise ValueError("GEMINI_API_KEY environment variable not set.")

genai.configure(api_key=GEMINI_API_KEY)

# Initialize the Gemini model
# You can choose different models based on your needs, e.g., 'gemini-1.5-pro-latest'
model = genai.GenerativeModel("gemini-2.0-flash")
chat_session = model.start_chat(history=[])

def speak(text):
  engine = pyttsx3.init()
  engine.say(text)
  engine.runAndWait()

def process_command(command):
  command_as_list = command.split()
  if len(command_as_list) == 2 and command_as_list[0].lower() == "open" and not command_as_list[1].__contains__("https"):
    speak(f"Opening {command_as_list[1]}")
    webbrowser.open(f"https://{command_as_list[1]}.com")
  elif len(command_as_list) == 2 and command_as_list[0].lower() == "open" and command_as_list[1].__contains__("https"):
    speak(f"Opening {command_as_list[1]}")
    webbrowser.open(command_as_list[1])
  elif len(command_as_list) > 2 and "open application" in command.lower():
    app_key = list(applications.keys())
    for i in range(len(applications)):
      if command.lower()[17:] in app_key[i].lower():
        file_path = applications[app_key[i]]
        os.startfile(file_path)
        break
  elif "hello jarvis" in command.lower():
    speak("Hello there! How can I help you today?")
  elif "what is your name" in command.lower():
    speak("I am Jarvis, your AI assistant.")
  else:
    # Let Gemini handle the request
    try:
        speak(f"Processing your request: {command}")
        response = chat_session.send_message(command) # Send message to Gemini
        gemini_response_text = response.text
        print(f"Jarvis: {gemini_response_text}")
        speak(gemini_response_text)
    except Exception as e:
        print(f"Error communicating with Gemini API: {e}")
        speak("I'm sorry, I encountered an error while processing your request.")
        

if __name__ == "__main__":
  speak("Initializing Jarvis.....")
  # Listen for the wake word "Jarvis"
  while True:
    command = input("Your input here: ")
    print("recognizing...")

    process_command(command)

    if (command.lower() == "jarvis"):
      speak("Ya, I am listening")
      print("Jarvis Active.....")