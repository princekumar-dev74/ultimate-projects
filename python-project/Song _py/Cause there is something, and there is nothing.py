import time
def type_lyric(line, char_delay=0.065):
    for char in line:
        print(char, end='', flush=True)
        time.sleep(char_delay)
    print()

    # follow @webkaizen

def print_lyrics():
    lyrics = [
          "Cause there is something, and there is nothing",
          "There is nothing in between",
          "And in my eyes, there is a tiny dancer",
          "Watching over me, he's singing",
          "She's a, she's a lady, and I am just a boy",
          "He's singing, She's a, she's a lady,",
          "and I am just a line without a hook",
]
    delays = [0.4, 1.8, 2.1, 2.4, 1.7, 2.0, 2.0]
    print("\n🎵 Now Playing - Line Without A Hook\n")
    time.sleep(1.5)
    for i, line in enumerate(lyrics):
        type_lyric(line)
        time.sleep(delays[i])

print_lyrics()
time.sleep(0.02)