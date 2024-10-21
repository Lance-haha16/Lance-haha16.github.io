from translate import Translator

initial_language=input("initisl lsngusge:").capitalize()
ultimate_language=input("ultimate language:").capitalize()
translator=Translator(initial_language,ultimate_language)
txt=input("请输入需要翻译的句子:")
translation=translator.translate(txt)
print(translation)
