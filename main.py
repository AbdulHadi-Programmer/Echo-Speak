import streamlit as st
import os
import uuid
import shutil
from gtts import gTTS
from googletrans import Translator

# Set page title
st.set_page_config(page_title="Echo Speak - AI Text-to-Speech", page_icon="🌍")
st.title("Echo Speak")

st.write("A text-to-speech app that converts text into speech in multiple languages with customizable voice settings.")

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
