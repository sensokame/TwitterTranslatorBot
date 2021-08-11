"""
 simple module for translation for now use translate library
 could change in the future
"""

from translate import Translator

def translate(text, to_lang, from_lang = "en"):
    """translate function to translate text from language to another"""
    translator = Translator(to_lang=to_lang, from_lang=from_lang)
    return translator.translate(text)

def _test():
    english_text = "This is a test."
    french_text = "Ceci est une épreuve."
    assert translate(english_text, "fr") == french_text
    assert translate(french_text, "en", "fr") == english_text


if __name__ == '__main__':
    _test()
