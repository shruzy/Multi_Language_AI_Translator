from deep_translator import GoogleTranslator

def translate_text(text, target_lang):

    try:
        translated = GoogleTranslator(source='auto', target=target_lang).translate(text)
    except:
        translated = text

    return translated