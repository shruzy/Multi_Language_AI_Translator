LANGUAGE_MAP = {
    "english": "en",
    "hindi": "hi",
    "marathi": "mr",
    "kannada": "kn",
    "tamil": "ta",
    "telugu": "te",
    "bengali": "bn",
    "gujarati": "gu",
    "punjabi": "pa",
    "malayalam": "ml",
    "urdu": "ur"
}

COMMAND_PHRASES = [
    "convert this into",
    "convert into",
    "translate this into",
    "translate into",
    "translate to",
    "say this in",
    "change to",
    "convert this in"
]


def parse_command(text):

    text_lower = text.lower()

    target_lang = "en"

    for lang in LANGUAGE_MAP:
        if lang in text_lower:
            target_lang = LANGUAGE_MAP[lang]

    cleaned_text = text_lower

    # remove command phrases
    for phrase in COMMAND_PHRASES:
        cleaned_text = cleaned_text.replace(phrase, "")

    # remove language name
    for lang in LANGUAGE_MAP:
        cleaned_text = cleaned_text.replace(lang, "")

    cleaned_text = cleaned_text.strip()

    return cleaned_text, target_lang