import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']


def english_to_french(english_word):
    """English to French translation"""

    url_lt=url
    apikey_lt=apikey
    version_lt='2018-05-01'
    authenticator = IAMAuthenticator(apikey_lt)
    language_translator = LanguageTranslatorV3(version=version_lt,authenticator=authenticator)
    language_translator.set_service_url(url_lt)
    lt = language_translator
    translation = lt.translate(text=english_word, model_id="en-fr").get_result()
    french_word = translation['translations'][0]['translation']

    if english_word == " ":
        print("Please enter a word")
    else:
        pass


    return french_word

def french_to_english(french_word):
    """French to English translation"""

    url_lt="https://api.au-syd.language-translator.watson.cloud.ibm.com/instances/d5d7bc93-3384-4f33-bd1b-45e082053127"
    apikey_lt="TIHuHIwrXDySRe1mT_o3SrKj98jYG5qHix2lBPtaUfJr"
    version_lt='2018-05-01'
    authenticator = IAMAuthenticator(apikey_lt)
    language_translator = LanguageTranslatorV3(version=version_lt,authenticator=authenticator)
    language_translator.set_service_url(url_lt)
    lt = language_translator
    translation = lt.translate(text=french_word, model_id="fr-en").get_result()
    english_word = translation['translations'][0]['translation']
    return english_word