from googletrans import Translator

french_words = ["Bonjour","Au revoir","Bienvenue","A bientôt"]

translator = Translator()
translations = {}

for word in french_words:
    translation = translator.translate(word, src='fr', dest='uk')
    translations[word] = translation.text

print(translations)