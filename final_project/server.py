from machinetranslation import translator
from flask import Flask, render_template, request
import json

app = Flask("Web Translator")

@app.route("/englishToFrench")
def englishToFrench():
    textToTranslate = request.args.get('textToTranslate')
    return render_template("index.html", french_word = textToTranslate)
    

@app.route("/frenchToEnglish")
def frenchToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    return render_template("index.html", french_word = textToTranslate)


@app.route("/")
def renderIndexPage():
    return "Hello"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
