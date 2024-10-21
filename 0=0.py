import tkinter as tk
from translate import Translator

def translate_text():
    initial_language = initial_lang_entry.get()
    ultimate_language = ultimate_lang_entry.get()
    text = text_entry.get("1.0", tk.END).strip()
    
    translator = Translator(from_lang=initial_language, to_lang=ultimate_language)
    try:
        translation = translator.translate(text)
        result_label.config(text=translation)
    except Exception as e:
        result_label.config(text=f"翻译时发生错误: {e}")

# 创建主窗口
root = tk.Tk()
root.title("翻译工具")

# 初始语言输入
tk.Label(root, text="初始语言代码（如 'en'）：").pack()
initial_lang_entry = tk.Entry(root)
initial_lang_entry.pack()

# 目标语言输入
tk.Label(root, text="目标语言代码（如 'fr'）：").pack()
ultimate_lang_entry = tk.Entry(root)
ultimate_lang_entry.pack()

# 文本输入框
tk.Label(root, text="请输入需要翻译的句子：").pack()
text_entry = tk.Text(root, height=5, width=40)
text_entry.pack()

# 翻译按钮
translate_button = tk.Button(root, text="翻译", command=translate_text)
translate_button.pack()

# 结果标签
result_label = tk.Label(root, text="", wraplength=400)
result_label.pack()

# 运行主循环
root.mainloop()
            
