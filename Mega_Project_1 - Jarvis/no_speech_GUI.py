import tkinter as tk
from tkinter import scrolledtext
import webbrowser
import pyttsx3
import google.generativeai as genai
import os
import threading # To run the Gemini interaction in a separate thread

# --- Configuration ---
# IMPORTANT: Ensure you have set the GEMINI_API_KEY environment variable.
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")
print(f"API Key found: {GEMINI_API_KEY}")

if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY environment variable not set. Please set it in your environment variables.")

genai.configure(api_key=GEMINI_API_KEY)

# Initialize the Gemini model
model = genai.GenerativeModel("gemini-2.0-flash")
chat_session = model.start_chat(history=[])

# Initialize text-to-speech engine
try:
    tts_engine = pyttsx3.init()
    # Optional: Adjust speaking rate
    # tts_engine.setProperty('rate', 150)
except Exception as e:
    print(f"Error initializing TTS engine: {e}")
    tts_engine = None

def speak(text):
    if tts_engine:
        tts_engine.say(text)
        tts_engine.runAndWait()
    else:
        print(f"TTS Engine not initialized. Speaking: {text}")

def process_command_and_respond(command):
    command_as_list = command.split()
    if len(command_as_list) == 2 and command_as_list[0].lower() == "open":
        website = command_as_list[1]
        if not website.__contains__("https"):
            url = f"https://{website}.com"
        else:
            url = website
        speak(f"Opening {website}")
        webbrowser.open(url)
        return f"Opened {website}"
    elif "hello jarvis" in command.lower():
        response_text = "Hello there! How can I help you today?"
        speak(response_text)
        return response_text
    elif "what is your name" in command.lower():
        response_text = "I am Jarvis, your AI assistant."
        speak(response_text)
        return response_text
    else:
        # Let Gemini handle the request
        speak(f"Processing your request: {command}")
        try:
            # Run Gemini interaction in a separate thread to keep the GUI responsive
            def get_gemini_response():
                try:
                    response = chat_session.send_message(command)
                    gemini_response_text = response.text
                    print(f"Jarvis: {gemini_response_text}")
                    speak(gemini_response_text)
                    # Update the GUI with the response
                    gui_output_area.configure(state='normal')
                    gui_output_area.insert(tk.END, f"Jarvis: {gemini_response_text}\n")
                    gui_output_area.configure(state='disabled')
                    gui_output_area.see(tk.END) # Auto-scroll to the bottom
                except Exception as e:
                    error_message = f"Error communicating with Gemini API: {e}"
                    print(error_message)
                    speak("I'm sorry, I encountered an error while processing your request.")
                    gui_output_area.configure(state='normal')
                    gui_output_area.insert(tk.END, f"Error: {error_message}\n")
                    gui_output_area.configure(state='disabled')
                    gui_output_area.see(tk.END)

            threading.Thread(target=get_gemini_response, daemon=True).start()
            return f"Processing: {command}..." # Immediate feedback to user

        except Exception as e:
            error_message = f"Error initiating Gemini request: {e}"
            print(error_message)
            speak("I'm sorry, I encountered an error while processing your request.")
            return f"Error: {error_message}"

# --- Tkinter GUI Setup ---
root = tk.Tk()
root.title("Jarvis AI Assistant")

# Input Frame
input_frame = tk.Frame(root, padx=10, pady=10)
input_frame.pack(fill=tk.X)

input_label = tk.Label(input_frame, text="Enter Command:", font=("Arial", 12))
input_label.pack(side=tk.LEFT)

command_entry = tk.Entry(input_frame, width=50, font=("Arial", 12))
command_entry.pack(side=tk.LEFT, padx=5)
command_entry.bind("<Return>", lambda event: send_command()) # Bind Enter key to send command

send_button = tk.Button(input_frame, text="Send", command=lambda: send_command(), font=("Arial", 10))
send_button.pack(side=tk.LEFT)

# Output Frame
output_frame = tk.Frame(root, padx=10, pady=10)
output_frame.pack(fill=tk.BOTH, expand=True)

output_label = tk.Label(output_frame, text="Assistant Output:", font=("Arial", 12))
output_label.pack(anchor=tk.W)

gui_output_area = scrolledtext.ScrolledText(output_frame, wrap=tk.WORD, width=60, height=15, font=("Arial", 11), state='disabled')
gui_output_area.pack(fill=tk.BOTH, expand=True)

def send_command():
    user_command = command_entry.get().strip()
    if not user_command:
        return # Do nothing if input is empty

    gui_output_area.configure(state='normal')
    gui_output_area.insert(tk.END, f"You: {user_command}\n")
    gui_output_area.configure(state='disabled')
    gui_output_area.see(tk.END) # Auto-scroll to the bottom
    command_entry.delete(0, tk.END) # Clear the input field

    # Process the command and get a response (immediate feedback)
    feedback = process_command_and_respond(user_command)
    if not feedback.startswith("Processing:"): # Don't add immediate "Processing" to output
        gui_output_area.configure(state='normal')
        gui_output_area.insert(tk.END, f"Assistant: {feedback}\n")
        gui_output_area.configure(state='disabled')
        gui_output_area.see(tk.END)

# Initial greeting
speak("Initializing Jarvis.....")
gui_output_area.configure(state='normal')
gui_output_area.insert(tk.END, "Jarvis: Initializing...\n")
gui_output_area.configure(state='disabled')

root.mainloop()