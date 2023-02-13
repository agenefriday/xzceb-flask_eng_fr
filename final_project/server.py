from machinetranslation import translator
from flask import Flask, render_template, request
import json

app = Flask("Web Translator")

@app.route("/englishToFrench")
def englishToFrench():
    textToTranslate = request.args.get('textToTranslate')
    def index():
        return render_template("templates/index.html", french_word = translator.english_to_french)
    
    return "Translated text to French"

@app.route("/frenchToEnglish")
def frenchToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    def index():
        return render_template("templates/index.html", french_word = translator.french_to_english)
    
    return "Translated text to English"

@app.route("/")
def renderIndexPage():
    def index():
    return render_template("templates/index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
