from translate import Translator

# Get initial and ultimate languages
initial_language = input("Initial language (e.g., 'en' for English): ")
ultimate_language = input("Ultimate language (e.g., 'fr' for French): ")

# Create a Translator object
translator = Translator(from_lang=initial_language, to_lang=ultimate_language)

# Input text to translate
txt = input("请输入需要翻译的句子: ")  # You can keep this prompt in Chinese

# Perform translation
translation = translator.translate(txt)

# Print the translation
print("Translation:", translation)
