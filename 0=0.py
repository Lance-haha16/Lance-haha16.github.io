import tkinter as tk
from translate import Translator

def translate_text():
    initial_language = initial_lang_entry.get().strip()
    ultimate_language = ultimate_lang_entry.get().strip()
    text = text_entry.get("1.0", tk.END).strip()

    if not initial_language or not ultimate_language or not text:
        result_label.config(text="请输入所有字段！")
        return

    translator = Translator(from_lang=initial_language, to_lang=ultimate_language)
    try:
        translation = translator.translate(text)
        result_label.config(text=translation)
    except Exception as e:
        result_label.config(text=f"翻译时发生错误: {e}")

def clear_text():
    initial_lang_entry.delete(0, tk.END)
    ultimate_lang_entry.delete(0, tk.END)
    text_entry.delete("1.0", tk.END)
    result_label.config(text="")

# 创建主窗口
root = tk.Tk()
root.title("翻译工具")
root.geometry("400x300")  # 设置窗口大小

# 设置字体
font_label = ("Arial", 10)
font_entry = ("Arial", 12)

# 初始语言输入
tk.Label(root, text="初始语言代码（如 'en'）：", font=font_label).grid(row=0, column=0, padx=10, pady=5, sticky='w')
initial_lang_entry = tk.Entry(root, font=font_entry)
initial_lang_entry.grid(row=0, column=1, padx=10, pady=5)

# 目标语言输入
tk.Label(root, text="目标语言代码（如 'fr'）：", font=font_label).grid(row=1, column=0, padx=10, pady=5, sticky='w')
ultimate_lang_entry = tk.Entry(root, font=font_entry)
ultimate_lang_entry.grid(row=1, column=1, padx=10, pady=5)

# 文本输入框
tk.Label(root, text="请输入需要翻译的句子：", font=font_label).grid(row=2, column=0, padx=10, pady=5, sticky='w')
text_entry = tk.Text(root, height=5, width=30, font=font_entry)
text_entry.grid(row=2, column=1, padx=10, pady=5)

# 翻译按钮
translate_button = tk.Button(root, text="翻译", command=translate_text, font=font_label)
translate_button.grid(row=3, column=0, padx=10, pady=10)

# 清除按钮
clear_button = tk.Button(root, text="清除", command=clear_text, font=font_label)
clear_button.grid(row=3, column=1, padx=10, pady=10)

# 结果标签
result_label = tk.Label(root, text="", wraplength=300, font=("Arial", 10))
result_label.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

# 运行主循环
root.mainloop()
