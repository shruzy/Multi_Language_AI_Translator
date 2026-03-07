import streamlit as st
import os
from audiorecorder import audiorecorder

from config import *
from modules.speech_to_text import audio_to_text
from modules.language_detector import detect_language
from modules.command_parser import parse_command
from modules.translator import translate_text
from modules.text_to_speech import text_to_audio


st.set_page_config(page_title="AI Voice Translator", page_icon="🎤", layout="wide")

st.title("🎤 AI Voice Translator")

# Chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Show chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Mic recorder
audio = audiorecorder("🎙 Record", "⏹ Stop")

if len(audio) > 0:

    audio_path = os.path.join(AUDIO_INPUT, "input.wav")
    audio.export(audio_path, format="wav")

    with st.spinner("Processing voice..."):

        # Speech → text
        text = audio_to_text(audio_path)

        # Detect language
        input_lang = detect_language(text)

        # Parse command
        clean_text, output_lang = parse_command(text)

        # Translate
        translated = translate_text(clean_text, output_lang)

        # Generate audio
        audio_file = text_to_audio(translated, output_lang, AUDIO_OUTPUT)
        output_audio = os.path.join(AUDIO_OUTPUT, audio_file)


    # USER CHAT BUBBLE - Only Voice Input section
    with st.chat_message("user"):
        st.markdown("**🎤 Your Voice Input**")
        st.audio(audio_path)
        st.markdown("**📝 Recognized Text**")
        st.write(text)


    # AI CHAT BUBBLE - Only Output Language section
    with st.chat_message("assistant"):
        st.markdown(f"**🌐 Output Language ({output_lang})**")
        st.write(translated)
        st.markdown("**🔊 Translated Voice**")
        st.audio(output_audio)


    # Update session state with simplified message
    ai_response = f"""
**Output Language ({output_lang}):**

{translated}
"""

    st.session_state.messages.append(
        {"role": "assistant", "content": ai_response}
    )

with st.sidebar:

    st.title("AI Translator")
    st.write("Voice to Voice Translation")

    st.divider()

    st.subheader("Supported Languages")

    languages = {
        "English": "en",
        "Hindi": "hi",
        "Marathi": "mr",
        "Tamil": "ta",
        "Telugu": "te",
        "Kannada": "kn",
        "Bengali": "bn",
        "Gujarati": "gu",
        "Punjabi": "pa",
        "Malayalam": "ml",
        "Urdu": "ur"
    }

    for lang in languages:
        st.write(f"• {lang}")