from tkinter import *
from deep_translator import GoogleTranslator

def translate_text():
    try:
        src_lang = src_lang_entry.get().strip()
        dest_lang = dest_lang_entry.get().strip()
        text = input_text.get("1.0", END).strip()

        if not text:
            output_text.delete("1.0", END)
            output_text.insert(END, "Please enter text to translate.")
            return

        translated = GoogleTranslator(source=src_lang, target=dest_lang).translate(text)
        output_text.delete("1.0", END)
        output_text.insert(END, translated)

    except Exception as e:
        output_text.delete("1.0", END)
        output_text.insert(END, f"Error: {str(e)}")

# GUI setup
root = Tk()
root.title("Language Translator")
root.geometry("400x400")

Label(root, text="Source Language Code (e.g., en):").pack()
src_lang_entry = Entry(root)
src_lang_entry.pack()

Label(root, text="Target Language Code (e.g., fr):").pack()
dest_lang_entry = Entry(root)
dest_lang_entry.pack()

Label(root, text="Enter text:").pack()
input_text = Text(root, height=5)
input_text.pack()

Button(root, text="Translate", command=translate_text).pack()

Label(root, text="Translated text:").pack()
output_text = Text(root, height=5)
output_text.pack()

root.mainloop()
