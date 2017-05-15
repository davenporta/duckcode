import warnings
warnings.filterwarnings("ignore")

from pydub import AudioSegment
from pydub.playback import play
import sys

try:
    mode = sys.argv[1]
except:
    mode = 'normal'

dot = AudioSegment.from_wav("dot2.wav")
dash = AudioSegment.from_wav("dash3.wav")
cspace = AudioSegment.from_wav("spacer2.wav")
startcode = AudioSegment.from_wav("start.wav")

sound = {'.': dot, '-': dash, ' ': cspace, '/': cspace}

code = {'A': '.-',     'B': '-...',   'C': '-.-.',
        'D': '-..',    'E': '.',      'F': '..-.',
        'G': '--.',    'H': '....',   'I': '..',
        'J': '.---',   'K': '-.-',    'L': '.-..',
        'M': '--',     'N': '-.',     'O': '---',
        'P': '.--.',   'Q': '--.-',   'R': '.-.',
        'S': '...',    'T': '-',      'U': '..-',
        'V': '...-',   'W': '.--',    'X': '-..-',
        'Y': '-.--',   'Z': '--..',

        '0': '-----',  '1': '.----',  '2': '..---',
        '3': '...--',  '4': '....-',  '5': '.....',
        '6': '-....',  '7': '--...',  '8': '---..',
        '9': '----.',

        '.': '.-.-.-', '!': '-.-.--', '?': '..--..',

        ' ': '/'}


def to_morse(s, mode):
    if s == '/quit':
        exit()
    if s == '/quackless':
        mode = 'nostart'
        play(dot)
        return mode
    phrase = ' '.join(code[i.upper()] for i in s)
    print("Sending: " + phrase)
    queue = [sound[c] for c in phrase]
    if mode == 'nostart':
        out = cspace
    else:
        out = startcode
    for char in queue:
        out += char
    play(out)
    print("Sent!")
    print("")
    return mode

print("")
print("Duck Code V1.1 by Alex Davenport")
print("--------------------------------")
print("Type /quit to exit and /quackless to remove start message")
print("")

while 1:
    mode = to_morse(input("Message to Send: "), mode)
