# import streamlit as st
# from gtts import gTTS
# import os

# # Streamlit UI
# st.title("🔊 EchoSpeak  Text-to-Speech (TTS) App")

# # Language selection
# language_options = {
#     "English": "en",
#     "French": "fr",
#     "Spanish": "es",
#     "German": "de",
#     "Hindi": "hi",
#     "Arabic": "ar"
# }
# language = st.selectbox("Select Language:", list(language_options.keys()))

# # Text input
# text = st.text_area("Enter text to speak:", "Hello, welcome to Streamlit!")

# if st.button("🎤 Convert & Play"):
#     if text.strip():  # Ensure text is not empty
#         tts = gTTS(text=text, lang=language_options[language])
#         filename = "output.mp3"
#         tts.save(filename)
        
#         # Play in Streamlit
#         st.audio(filename, format="audio/mp3")
#     else:
#         st.warning("Please enter some text to convert to speech!")

#####################################################################################################################################################################################################################
#####################################################################################################################################################################################################################
#####################################################################################################################################################################################################################

# import streamlit as st
# import os
# import uuid
# from gtts import gTTS

# # Directory for saving audio files
# SAVE_DIR = "generated_audio"
# if not os.path.exists(SAVE_DIR):
#     os.makedirs(SAVE_DIR)

# HISTORY_FILE = "history.txt"

# # Streamlit App Title
# st.title("🔊 Echo Speak - Text to Speech")

# # Text Input Section
# title = st.text_input("Enter a title for your audio:")
# text_input = st.text_area("Enter text to convert to speech:")

# # Language Selection
# languages = {
#     "English": "en",
#     "Spanish": "es",
#     "French": "fr",
#     "German": "de",
#     "Italian": "it",
#     "Hindi": "hi",
#     "Urdu": "ur"
# }
# language = st.selectbox("Select Language", list(languages.keys()))

# # Convert Text to Speech
# if st.button("Convert & Play"):
#     if text_input.strip():
#         unique_id = uuid.uuid4().hex[:8]  # Generate a unique ID
#         filename = f"{SAVE_DIR}/{unique_id}.mp3"
#         tts = gTTS(text=text_input, lang=languages[language])
#         tts.save(filename)

#         # Save history in a valid format
#         with open(HISTORY_FILE, "a") as file:
#             file.write(f"{title if title.strip() else 'Untitled'}|{filename}|{unique_id}\n")

#         # Play & Download
#         st.audio(filename, format="audio/mp3")
#         st.download_button(label="Download Audio", data=open(filename, "rb"), file_name=f"{title}.mp3" if title.strip() else "EchoSpeak.mp3", mime="audio/mp3", key=unique_id)

# # Show History
# st.subheader("🕰️ Previous Conversations")
# if os.path.exists(HISTORY_FILE):
#     with open(HISTORY_FILE, "r") as file:
#         history_lines = file.read().splitlines()[-5:]  # Show last 5 saved files

#     for line in reversed(history_lines):
#         parts = line.split("|")
#         if len(parts) == 3:  # Ensure correct format
#             title, audio_file, unique_id = parts
#             if os.path.exists(audio_file):
#                 st.markdown(f"**{title}**")
#                 st.audio(audio_file, format="audio/mp3")
#                 st.download_button(label="Download", data=open(audio_file, "rb"), file_name=f"{title}.mp3", mime="audio/mp3", key=f"download_{unique_id}")

# ## Perfect Code but some changes need: 
# import streamlit as st
# import os
# import uuid
# import shutil
# from gtts import gTTS
# from googletrans import Translator

# # # Set page title
# # st.title("🔊 Echo Speak - Text to Speech", page_icon)
# # App Branding
# st.set_page_config(page_title="Echo Speak - AI Text-to-Speech", page_icon="🌍")
# st.title("Echo Speak - AI Text-to-Speech")

# # Initialize translator
# translator = Translator()

# # Create a directory for saving audio files
# AUDIO_DIR = "saved_audio"
# os.makedirs(AUDIO_DIR, exist_ok=True)

# # Language selection dropdown
# languages = {
#     "English": "en",
#     "Urdu": "ur",
#     "French": "fr",
#     "German": "de",
#     "Italian": "it",
#     "Spanish": "es"
# }

# # Title input for saving the file
# title_input = st.text_input("Enter a title for the saved audio:")

# # Input text
# text_input = st.text_area("Enter text to convert into speech:", height=200)

# # Select the Language :
# selected_language = st.selectbox("Select Language:", list(languages.keys()))

# # Function to generate speech
# def generate_speech(text, lang_code, file_name):
#     tts = gTTS(text=text, lang=lang_code)
#     tts.save(file_name)

# # Button to convert text to speech
# if st.button("Generate Speech 🎙️"):
#     if text_input:
#         translated_text = text_input  # Default text is the input text

#         # If selected language is not English, translate first
#         if selected_language != "English":
#             translated_text = translator.translate(text_input, dest=languages[selected_language]).text
        
#         # Generate unique filename
#         unique_id = str(uuid.uuid4())[:8]  # Generate short UUID
#         file_name = f"{AUDIO_DIR}/{unique_id}.mp3"

#         # Generate speech
#         generate_speech(translated_text, languages[selected_language], file_name)

#         # Save history
#         history_file = "history.txt"
#         with open(history_file, "a", encoding="utf-8") as f:
#             f.write(f"{title_input}|{file_name}\n")

#         # Display and allow download
#         st.audio(file_name, format="audio/mp3")
#         st.download_button("Download 🎧", data=open(file_name, "rb"), file_name=f"{title_input}.mp3", mime="audio/mp3", key=unique_id)

#     else:
#         st.warning("⚠️ Please enter some text to generate speech!")

# # Section to show previously saved audio files
# st.subheader("📜 Previously Generated Audio")

# history_file = "history.txt"
# if os.path.exists(history_file):
#     with open(history_file, "r", encoding="utf-8") as f:
#         history_data = f.readlines()

#     if history_data:
#         for line in history_data:
#             try:
#                 title, audio_file = line.strip().split("|")
#                 st.write(f"{title}")
#                 st.audio(audio_file, format="audio/mp3")
#                 st.download_button("⬇️ Download", data=open(audio_file, "rb"), file_name=f"{title}.mp3", mime="audio/mp3", key=str(uuid.uuid4()))
#             except ValueError:
#                 continue  # Skip invalid lines

#     if not history_data:
#         st.info("No saved audio found.")
# else:
#     st.info("No saved audio found.")

import streamlit as st
import os
import uuid
import shutil
from gtts import gTTS
from googletrans import Translator

# Set page title
st.set_page_config(page_title="Echo Speak - AI Text-to-Speech", page_icon="🌍")
st.title("Echo Speak - AI Text-to-Speech")

# Initialize translator
translator = Translator()

# Create a directory for saving audio files
AUDIO_DIR = "saved_audio"
os.makedirs(AUDIO_DIR, exist_ok=True)

# Language selection dropdown
languages = {
    "English": "en",
    "Urdu": "ur",
    "French": "fr",
    "German": "de",
    "Italian": "it",
    "Spanish": "es"
}

# Title input for saving the file
title_input = st.text_input("Enter a title for the saved audio:")

# Input text
text_input = st.text_area("Enter text to convert into speech:", height=200)

# Select the Language :
selected_language = st.selectbox("Select Language:", list(languages.keys()))

# Function to generate speech
def generate_speech(text, lang_code, file_name):
    tts = gTTS(text=text, lang=lang_code)
    tts.save(file_name)

# Button to convert text to speech
if st.button("Generate Speech 🎧"):
    if text_input:
        translated_text = text_input  # Default text is the input text

        # If selected language is not English, translate first
        if selected_language != "English":
            translated_text = translator.translate(text_input, dest=languages[selected_language]).text
        
        # Generate unique filename
        unique_id = str(uuid.uuid4())[:8]  # Generate short UUID
        file_name = f"{AUDIO_DIR}/{unique_id}.mp3"

        # Generate speech
        generate_speech(translated_text, languages[selected_language], file_name)

        # Save history
        history_file = "history.txt"
        with open(history_file, "a", encoding="utf-8") as f:
            f.write(f"{title_input}|{file_name}\n")

        # Display and allow download
        st.audio(file_name, format="audio/mp3")
        st.download_button("Download 🎧", data=open(file_name, "rb"), file_name=f"{title_input}.mp3", mime="audio/mp3", key=unique_id)
    else:
        st.warning("⚠️ Please enter some text to generate speech!")

# Section to show previously saved audio files
st.subheader("📜 Previously Generated Audio")

history_file = "history.txt"
if os.path.exists(history_file):
    with open(history_file, "r", encoding="utf-8") as f:
        history_data = f.readlines()

    if history_data:
        updated_history = []
        for line in history_data:
            try:
                title, audio_file = line.strip().split("|")
                st.write(f"{title}")
                st.audio(audio_file, format="audio/mp3")
                st.download_button("⬇️ Download", data=open(audio_file, "rb"), file_name=f"{title}.mp3", mime="audio/mp3", key=str(uuid.uuid4()))
                
                # Add delete buttont
                if st.button(f"❌ Delete", key=audio_file):
                    os.remove(audio_file)
                else:
                    updated_history.append(line)
            except ValueError:
                continue  # Skip invalid lines

        # Update history file after deletion
        with open(history_file, "w", encoding="utf-8") as f:
            f.writelines(updated_history)

    if not history_data:
        st.info("No saved audio found.")
else:
    st.info("No saved audio found.")
