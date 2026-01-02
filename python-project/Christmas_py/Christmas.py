import tkinter as tk
import random

# Setup window
root = tk.Tk()
root.title("🎄 Christmas Tree Typing Animation 🎶")
root.configure(bg="black")
root.geometry("700x520")

canvas = tk.Canvas(root, width=700, height=520, bg="black", highlightthickness=0)
canvas.pack()

# Tree structure
tree_lines = [
    "          *         ",
    "         ***        ",
    "        *****       ",
    "       *******      ",
    "     ***********    ",
    "    *************   ",
    "   ***************  ",
    "  ***************** ",
    "         ***        ",
    "         ***        ",
    "         ***        "
]

# Blinking colors for lights
colors = ["red", "green", "yellow", "cyan", "magenta", "orange"]

# Lyrics (each line will type word by word)
lyrics = [
    "♪ Jingle bells, jingle bells,",
    "Jingle all the way! ♪",
    "Oh, what fun it is to ride",
    "In a one-horse open sleigh! ♪",
    "",
    "♪ Dashing through the snow,",
    "On a one-horse open sleigh,",
    "Over the fields we go,",
    "Laughing all the way! ♪",
    "",
    "🎅 Merry Christmas Boss 🎅"
]

current_line = 0
current_text = ""
text_obj = None

def draw_tree():
    canvas.delete("tree")
    y = 50
    for line in tree_lines:
        x = 200 - (len(line) * 6)
        for char in line:
            if char == "*":
                color = random.choice(colors)
                canvas.create_text(x, y, text="★", fill=color, font=("Arial", 16, "bold"), tags="tree")
            x += 12
        y += 25

# Tree text
    canvas.create_text(200, 420, text="🎄 Merry Christmas 🎄", fill="white", font=("Comic Sans MS", 18, "bold"))

def type_lyrics():
    global current_line, current_text, text_obj

    if current_line >= len(lyrics):
        return

    full_line = lyrics[current_line]
    if len(current_text) < len(full_line):
        # Add one more character
        current_text += full_line[len(current_text)]
        # Delete and reprint
        canvas.delete("lyric")
        canvas.create_text(520, 100 + current_line * 25,
                           text=current_text, fill="lightgreen",
                           font=("Georgia", 12, "italic"),
                           anchor="center", tags="lyric")
        root.after(100, type_lyrics)  # speed of typing (ms)
    else:
        # Move to next line after a small pause
        current_line += 1
        current_text = ""
        root.after(800, type_lyrics)


def animate_tree():
    draw_tree()
    root.after(500, animate_tree)

# Start animations
animate_tree()
root.after(1000, type_lyrics)

root.mainloop()
