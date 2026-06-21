import streamlit as st
from deep_translator import GoogleTranslator
from gtts import gTTS
import os

st.set_page_config(page_title="Language Translator", layout="centered")
st.title("🌍 AI Language Translation Tool")

text = st.text_area("Enter text to translate:", height=150)

langs = {
    "English": "en",
    "Hindi": "hi",
    "Spanish": "es",
    "French": "fr",
    "German": "de",
    "Chinese (Simplified)": "zh-cn",
    "Arabic": "ar",
    "Japanese": "ja"
}

col1, col2 = st.columns(2)
with col1:
    src_lang = st.selectbox("Source Language", list(langs.keys()))
with col2:
    tgt_lang = st.selectbox("Target Language", list(langs.keys()))

if st.button("Translate"):
    if text:
        try:
            # Deep Translator ka naya tareeqa
            translated_text = GoogleTranslator(
                source=langs[src_lang], 
                target=langs[tgt_lang]
            ).translate(text)
            
            st.success("✅ Translation:")
            st.write(translated_text)

            # Text-to-Speech (yeh waisa hi hai)
            if st.button("🔊 Listen to Translation"):
                tts = gTTS(translated_text, lang=langs[tgt_lang])
                tts.save("translation.mp3")
                st.audio("translation.mp3", format="audio/mp3")
                os.remove("translation.mp3")
        except Exception as e:
            st.error(f"Error: {e}")
    else:
        st.warning("Please enter some text.")