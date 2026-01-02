import time
import sys
def type_lyric(line, char_delay=0.065):
    for char in line:
        print(char, end='', flush=True)
        time.sleep(char_delay)
    print()

# FOLLOW @webkaizen

def print_lyrics():
    lyrics = [
           "All I dream of is your eyes",
           "All I long for is your touch",
           "And darlin',",
           "something tells me",
           "it's enough,",
           "mmm",
           "You can say that I'm a fool",
           "And I don't know very much",
           "But I think",
           "they call",
           "this love",
    ]
    delays = [1.6, 1.4, 1.8, 2.1, 2.4, 1.7, 2.0, 2.0, 1.5, 1.5, 2.5]
    print("\n I Think They Call This Love Lyrics: \n")
    time.sleep(1.5)
    for i, line in enumerate(lyrics):
        type_lyric(line)
        time.sleep(delays[i])

print_lyrics()