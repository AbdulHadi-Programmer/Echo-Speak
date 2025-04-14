import streamlit as st
from deep_translator import GoogleTranslator

# Streamlit page configuration
st.set_page_config(page_title="Multi-Language Translator", page_icon="🌍")

# App title
st.title("🌍 Multi-Language Translator")

# Language options for translation
languages = {
    "English": "en",
    "Urdu": "ur",
    "French": "fr",
    "German": "de",
    "Italian": "it",
    "Spanish": "es",
    "Chinese": "zh-cn",
    "Hindi": "hi",
    "Arabic": "ar",
    "Portuguese": "pt"
}

# User input text area
text_input = st.text_area("📝 Enter text in any language:", height=150)

# Convert button
if st.button("🔍 Detect & Convert"):
    if text_input.strip():
        # Auto-detect source language
        detected_lang = GoogleTranslator(source="auto", target="en").detect(text_input)
        
        # Show detected language
        st.success(f"Detected Language: **{detected_lang.upper()}**")

        # Language selection dropdown
        selected_language = st.selectbox("🌐 Select target language:", list(languages.keys()))

        # Translate the text
        translated_text = GoogleTranslator(source="auto", target=languages[selected_language]).translate(text_input)

        # Show translated text
        st.text_area("✅ Translated Text:", translated_text, height=150)
    else:
        st.warning("⚠️ Please enter some text to translate!")
