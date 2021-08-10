# simple module for translation for now use translate library
# could change in the future
from translate import Translator

def translate(text, to, fro = "en"):
    translator = Translator(to_lang=to, from_lang=fro)
    return translator.translate(text)

def _test():
    en = "This is a test."
    fr = "Ceci est une épreuve."
    assert translate(en, "fr") == fr
    assert translate(fr, "en", "fr") == en


if __name__ == '__main__':
    _test()