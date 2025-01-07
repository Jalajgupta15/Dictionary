import tkinter as tk
from tkinter import ttk
from nltk.corpus import wordnet as wn
import nltk

# Ensure NLTK data is downloaded
nltk.download('wordnet')

def result(*args):
    word = text_entry.get().strip()
    if word:
        synsets = wn.synsets(word)
        if synsets:
            label1['text'] = word.capitalize()
            label2['text'] = ", ".join(set([syn.lexname().split('.')[0] for syn in synsets]))

            meaning_string = ''
            for syn in synsets[:3]:  # Get meanings from the first 3 synsets
                meaning_string += f"- {syn.definition()}\n"
            label3['text'] = meaning_string.strip()
            label3.config(fg='#000000')
        else:
            label1['text'] = word.capitalize()
            label2['text'] = "No Such Word"
            label3.config(fg='red')
            label3['text'] = f"We can't find any match for word =>\n\"{word}\""

# GUI Setup
root = tk.Tk()
root.title("Python Dictionary")
root.resizable(0, 0)
root.geometry("300x200")
root.config(bg='white')

text_entry = ttk.Entry(root, width=20, font=("Sitka Small", 11), justify=tk.CENTER)
text_entry.bind("<Return>", result)
text_entry.place(x=10, y=21)

search_btn = tk.Button(root, text="Search", bg='#8c52ff', fg='#ffffff', font=("Sitka Small", 9),
                       width=7, relief=tk.FLAT, command=result)
search_btn.place(x=220, y=20)

output_frame = tk.Frame(root, bg='#ffffff')
output_frame.place(x=10, y=70, height=120, width=280)

label1 = tk.Label(output_frame, font=("Arial", 12, 'bold'), bg='#ffffff')
label1.place(x=10, y=5)

label2 = tk.Label(output_frame, font=("Sitka Small", 6, 'italic'), justify=tk.LEFT, fg='#a6a6a6', bg='#ffffff')
label2.place(x=10, y=30)

label3 = tk.Message(output_frame, width=250, font=("Sitka Small", 8),
                    bg='#ffffff', justify=tk.LEFT)
label3.place(x=10, y=45)

root.mainloop()
