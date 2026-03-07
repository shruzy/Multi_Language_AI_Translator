import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

AUDIO_INPUT = os.path.join(BASE_DIR, "data/audio_input")
EXTRACTED_TEXT = os.path.join(BASE_DIR, "data/extracted_text")
COMMAND_DATA = os.path.join(BASE_DIR, "data/command_data")
TRANSLATED_TEXT = os.path.join(BASE_DIR, "data/translated_text")
AUDIO_OUTPUT = os.path.join(BASE_DIR, "static/audio_output")

FASTTEXT_MODEL = os.path.join(BASE_DIR, "models/lid.176.bin")