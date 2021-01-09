from flask import Flask,request,jsonify
from textblob import  TextBlob
from googletrans import Translator

app = Flask(__name__)

@app.route('/spellchecker',methods = ['POST'])
def spellChecker():
    text = request.get_json()['text']
    correctedText = TextBlob(text).correct()
    return jsonify({'text' : str(correctedText)}),200


@app.route('/translator',methods = ['POST'])
def translator():
    text_to_convert = request.get_json()['text']
    translator = Translator()
    translations = {}
    return jsonify({'text' : str(translator.translate(text_to_convert).text)}),200

app.run()




