import time
import sys
def type_lyric(line, char_delay=0.065):
    for char in line:
        print(char, end='', flush=True)
        time.sleep(char_delay)
    print()

    # follow @webkaizen

def print_lyrics():
    lyrics = [
        "Mein ab kyun hosh may aata nahi?",
        "Sukoon yeh dil kyun paata nahi?",
        "Kyun torrun khud se jo thay waaday",
        "Ke ab yeh ishq nibhaana nahi?",
        "Mein morrun tum se jo yeh chehra",
        "Dobara nazar milana nahi",
        "Yeh duniya jaanay mera dard",
        "Tujhe yeh nazar kyun aata nahi?",
    ]
    delays = [1.6, 1.4, 1.8, 2.1, 2.4, 1.7, 2.0, 2.0]
    print("One last message to you ❤‍🩹:\n")
    time.sleep(1.5)
    for i, line in enumerate(lyrics):
        type_lyric(line)
        time.sleep(delays[i])

print_lyrics()
time.sleep(0.02)