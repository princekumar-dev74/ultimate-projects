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
           "Teri nazron ka dil pe hua hai asar,",
           "Tu mera mehboob hai jaana",
           "Teri ulfat mein jeeta har pal",
           "Tu ik tohfa hai khuda ka",
    ]
    delays = [1.6, 1.4, 1.8, 2.1]
    print("\n 🎵 Now Playing - Ehsaas💔 \n")
    time.sleep(1.5)
    for i, line in enumerate(lyrics):
        type_lyric(line)
        time.sleep(delays[i])

print_lyrics()