import speech_recognition as sr
import webbrowser
import pyttsx3
import google.generativeai as genai
import os

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

recognizer = sr.Recognizer()

def speak(text):
  engine = pyttsx3.init()
  engine.say(text)
  engine.runAndWait()

def process_command(command):
  command_as_list = command.split()
  if len(command_as_list) == 2 and command_as_list[0] == "open":
    speak(f"Openin {command_as_list[1]}")
    webbrowser.open(f"https://{command_as_list[1]}.com")
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
        print(f"Gemini: {gemini_response_text}")
        speak(gemini_response_text)
    except Exception as e:
        print(f"Error communicating with Gemini API: {e}")
        speak("I'm sorry, I encountered an error while processing your request.")
        

if __name__ == "__main__":
  speak("Initializing Jarvis.....")
  # Listen for the wake word "Jarvis"
  while True:
    print("recognizing...")
    try:
      with sr.Microphone() as source:
        print("Listening.....")
        audio = recognizer.listen(source, timeout=2, phrase_time_limit=1)

      # recognize speech using Sphinx
      command = recognizer.recognize_google(audio)
      print(command)

      process_command(command)

      if (command.lower() == "jarvis"):
        speak("Ya, I am listening")
        print("Jarvis Active.....")

        try:
          with sr.Microphone() as source:
            print("Listening for command...")
            audio_command = recognizer.listen(source, timeout=5, phrase_time_limit=10) # Listen for the command
          actual_command = recognizer.recognize_google(audio_command)
          print(f"Command received: {actual_command}")
          process_command(actual_command)

        except sr.WaitTimeoutError:
          speak("I didn't hear a command. Please try again.")
          print("No command received after wake word.")
        except Exception as e:
          print(f"Error recognizing command: {e}")
          speak("Sorry, I couldn't understand that command.")

    except Exception as e:
        print("Error; {0}".format(e))