from textblob import  TextBlob

class SpellChecker():
    def post(self,text):
        print(text)
        return TextBlob(text).correct()