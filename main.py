from tkinter import *
from tkinter import ttk, messagebox
import googletrans
from googletrans import Translator
from langdetect import detect, LangDetectException

# Initialize the main window
root = Tk()
root.geometry('1080x500')
root.resizable(0, 0)
root.title("Language Translator")
root.config(bg='#cff4fa')


def clear_all():
    text1.delete(1.0, END)
    text2.delete(1.0, END)


def label_change():
    c = combo1.get()
    c1 = combo2.get()
    label1.configure(text=c)
    label2.configure(text=c1)
    root.after(1000, label_change)


def translate_text(text, src_lang, dest_lang):
    try:
        translator = Translator()
        translated = translator.translate(text, src=src_lang, dest=dest_lang)
        return translated.text
    except Exception as e:
        messagebox.showerror("Translation Error", f"An error occurred during translation: {e}")
        return None


def translate_now():
    try:
        text_ = text1.get(1.0, END).strip()
        c3 = combo2.get()
        if text_:
            try:
                src_lang = detect(text_)
            except LangDetectException as e:
                messagebox.showerror("Language Detection Error",
                                     f"Could not detect the language of the input text: {e}")
                return

            target_language_code = None
            for code, lang in language.items():
                if lang == c3:
                    target_language_code = code
                    break

            if target_language_code:
                translated_text = translate_text(text_, src_lang, target_language_code)
                if translated_text is not None:
                    text2.delete(1.0, END)
                    text2.insert(END, translated_text)
            else:
                messagebox.showerror("Language Error", "Selected language not found in the translation service.")
        else:
            messagebox.showwarning("Input Error", "Please enter text to translate.")
    except Exception as e:
        messagebox.showerror("Error", f"An unexpected error occurred: {e}")


# icon_image
image_icon = PhotoImage(file="icon.png")
root.iconphoto(False, image_icon)

# Arrow icon
arrow_image = PhotoImage(file="translate.png")
image_label = Label(root, image=arrow_image, width=70, height=70)
image_label.place(x=510, y=40)

# Language setup
language = googletrans.LANGUAGES
languageV = list(language.values())
lang1 = language.keys()

# Combo boxes and labels
combo1 = ttk.Combobox(root, values=languageV, font="Roboto 14", state="r")
combo1.place(x=118, y=50)
combo1.set("English")

label1 = Label(root, text="English", font="segoe 24 bold", bg="#cfd0d4", width=15, bd=4, relief=GROOVE)
label1.place(x=90, y=100)

f = Frame(root, bg="grey", bd=5)
f.place(x=30, y=170, width=410, height=225)

text1 = Text(f, font="Roboto 20", bg="white", relief=GROOVE, wrap=WORD)
text1.place(x=0, y=0, width=400, height=215)

scrollbar1 = Scrollbar(f)
scrollbar1.pack(side="right", fill="y")
scrollbar1.configure(command=text1.yview)
text1.configure(yscrollcommand=scrollbar1.set)

combo2 = ttk.Combobox(root, values=languageV, font="Roboto 14", state="r")
combo2.place(x=740, y=50)
combo2.set("Selected Language")

label2 = Label(root, text="English", font="segoe 24 bold", bg="#cfd0d4", width=15, bd=4, relief=GROOVE)
label2.place(x=710, y=100)

f1 = Frame(root, bg="grey", bd=5)
f1.place(x=640, y=170, width=410, height=225)

text2 = Text(f1, font="Roboto 20", bg="white", relief=GROOVE, wrap=WORD)
text2.place(x=0, y=0, width=400, height=215)

scrollbar2 = Scrollbar(f1)
scrollbar2.pack(side="right", fill="y")
scrollbar2.configure(command=text2.yview)
text2.configure(yscrollcommand=scrollbar2.set)

# Translate button
translate = Button(root, text="Translate", font="Roboto 15 bold italic",
                   activebackground="green", cursor="hand2", bd=5,
                   bg="#fc4935", fg="black", command=translate_now)
translate.place(x=420, y=420)

# Clear_all button
clear = Button(root, text="Clear", font="Roboto 15 bold italic",
               activebackground="green", cursor="hand2", bd=5,
               bg="white", fg="black", command=clear_all)
clear.place(x=580, y=420)

label_change()

root.mainloop()
