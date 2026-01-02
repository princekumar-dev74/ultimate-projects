import tkinter as tk
lyrics = [
    "Uski Aankhon Mein Faila Kajal",
    "Baaton Se Karti Ghayal",
    "Sanson Mein Uska Hi Hai Naam",
    "Meri Neende Udi Hai Jab Se",
    "Tu Aa Gayi Jeevan Mein",
    "Raushan Kar De Tu Mujhko Aaj",
]
delays = [1.6, 1.4, 1.8, 2.1, 2.4, 1.7]  # seconds
colors = ["#8e2828", "#2b4162", "#d79922", "#f13c20", "#4056a1", "#0b3954"]

root = tk.Tk()
root.geometry("800x300")
root.title("Lyrics Player")
root.resizable(False, False)

label = tk.Label(root, text="", font=("Georgia", 28, "bold"), fg="white", bg="black", pady=30)
label.pack(expand=True, fill="both")

def type_lyric(line, line_index, char_index=0):
    if char_index <= len(line):
        label.config(text=line[:char_index])
        root.after(65, lambda: type_lyric(line, line_index, char_index+1))  # 65 ms per char
    else:
        ms_delay = int(delays[line_index] * 1000)
        root.after(ms_delay, lambda: show_lyrics(line_index+1))

def show_lyrics(index=0):
    if index < len(lyrics):
        bg_color = colors[index % len(colors)]
        root.config(bg=bg_color)
        label.config(bg=bg_color)
        type_lyric(lyrics[index], index)
    else:
        label.config(text="🎵 Now Playing - Kashish")
        root.config(bg="black")
        label.config(bg="black")

show_lyrics()

root.mainloop()