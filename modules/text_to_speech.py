from gtts import gTTS
import os

SUPPORTED = ["en","hi","mr","ta","te","kn","bn","gu","pa","ml","ur"]

def text_to_audio(text, lang, output_folder):

    if lang not in SUPPORTED:
        lang = "en"

    filename = "output.mp3"
    path = os.path.join(output_folder, filename)

    tts = gTTS(text=text, lang=lang)
    tts.save(path)

    return filename