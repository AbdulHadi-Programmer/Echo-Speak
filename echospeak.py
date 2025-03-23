import streamlit as st
import pyttsx3
import os
import uuid
import time
import shutil
import subprocess

# App Branding
st.set_page_config(page_title="Echo Speak - AI Text-to-Speech", page_icon="🎙️")

# Initialize TTS engine
engine = pyttsx3.init()

# Set up storage folder for generated audio
AUDIO_DIR = "saved_audio"
os.makedirs(AUDIO_DIR, exist_ok=True)  # Create folder if not exists

# Get available voices
voices = engine.getProperty("voices")
voice_options = [f"{i}: {voice.name}" for i, voice in enumerate(voices)]

# Predefined speed options
speed_options = {"Very Slow": 80, "Slow": 120, "Normal": 150, "Fast": 200, "Very Fast": 250}

# Available formats (Including MP3)
audio_formats = ["wav", "ogg", "flac", "mp3"]
if not shutil.which("ffmpeg"):  # Check if FFmpeg is installed
    audio_formats.remove("mp3")  # Remove MP3 if not available

# Function to generate speech
def generate_audio(title, text, rate, volume, voice_index, audio_format):
    engine.setProperty("rate", rate)
    engine.setProperty("volume", volume)

    if 0 <= voice_index < len(voices):
        engine.setProperty("voice", voices[voice_index].id)

    unique_id = uuid.uuid4().hex[:8]
    filename_base = f"{title.replace(' ', '_')}_{unique_id}"
    filename_wav = f"{filename_base}.wav"
    filepath_wav = os.path.join(AUDIO_DIR, filename_wav)

    engine.save_to_file(text, filepath_wav)
    engine.runAndWait()  # Process the speech before returning

    time.sleep(1)  # Give system time to write the file
    if os.path.exists(filepath_wav):
        if audio_format == "mp3":
            filename_mp3 = f"{filename_base}.mp3"
            filepath_mp3 = os.path.join(AUDIO_DIR, filename_mp3)

            if shutil.which("ffmpeg"):
                cmd = f'ffmpeg -i "{filepath_wav}" -q:a 2 "{filepath_mp3}" -y'
                subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

                if os.path.exists(filepath_mp3):
                    os.remove(filepath_wav)  # Remove original WAV file
                    return filename_mp3, filepath_mp3
                else:
                    st.error("⚠️ MP3 conversion failed. Try using another format.")
                    return filename_wav, filepath_wav
            else:
                st.warning("⚠️ FFmpeg not found! MP3 conversion unavailable.")
                return filename_wav, filepath_wav

        elif audio_format != "wav":
            filename_converted = f"{filename_base}.{audio_format}"
            filepath_converted = os.path.join(AUDIO_DIR, filename_converted)
            shutil.copy(filepath_wav, filepath_converted)  # Copy file without re-encoding
            os.remove(filepath_wav)  # Remove original WAV file
            return filename_converted, filepath_converted

        return filename_wav, filepath_wav
    else:
        st.error("⚠️ Audio file was not generated correctly. Please try again.")
        return None, None

# Load history in session state (Permanent storage)
if "history" not in st.session_state:
    st.session_state.history = []

# Streamlit UI with Branding
st.title("🎙️ Echo Speak - AI Text-to-Speech")
st.markdown("Convert text into high-quality speech with multiple voice options, adjustable speed, and different audio formats!")

# Title Input Field
title = st.text_input("Enter a title for your audio file:", "")

# **Larger Text Input**
text = st.text_area("Enter text to convert to speech:", "Hello, this is a test!", height=250)

# **Voice Selection**
selected_voice = st.selectbox("Select Voice", voice_options)
voice_index = int(selected_voice.split(":")[0])

# **Speech Rate Selection**
selected_speed = st.radio("Select Speech Speed", list(speed_options.keys()), index=2)
rate = speed_options[selected_speed]

# **Volume Control**
volume = st.slider("Volume", 0.1, 1.0, 1.0)

# **Audio Format Selection (MP3 Included)**
selected_format = st.radio("Select Audio Format", audio_formats, index=0)

# **Show warning if MP3 is selected but FFmpeg is missing**
if selected_format == "mp3" and not shutil.which("ffmpeg"):
    st.warning("⚠️ MP3 conversion requires FFmpeg. Please install it to use MP3 format.")

# **Generate Speech Button**
if st.button("🎤 Generate Speech"):
    if text.strip():
        if not title.strip():
            st.warning("⚠️ Please enter a title!")
        else:
            filename, audio_file = generate_audio(title, text, rate, volume, voice_index, selected_format)

            if audio_file:
                st.session_state.history.append(
                    {"title": title, "text": text[:30] + "...", "file": audio_file, "filename": filename}
                )

                if os.path.exists(audio_file):
                    st.audio(audio_file, format=f"audio/{selected_format}")

# **Show Previous Conversions**
st.subheader("📜 Saved Audio Files")

if st.session_state.history:
    for item in reversed(st.session_state.history):  # Show all saved files
        with st.container():
            st.markdown(f"**🎙️ {item['title']}**", unsafe_allow_html=True)

            if os.path.exists(item["file"]):
                st.audio(item["file"], format=f"audio/{selected_format}")

                # Download Button
                with open(item["file"], "rb") as file:
                    st.download_button("📥 Download", file, file_name=item["filename"], mime=f"audio/{selected_format}")
            else:
                st.warning(f"⚠️ File `{item['filename']}` is missing.")
