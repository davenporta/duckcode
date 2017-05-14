import warnings
warnings.filterwarnings("ignore")

from pydub import AudioSegment
from pydub.playback import play

dot = AudioSegment.from_wav("dot2.wav")
dash = AudioSegment.from_wav("dash2.wav")
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

        ' ': '/'}

def to_morse(s):
    if s == '/quit':
        exit()
    phrase = ' '.join(code[i.upper()] for i in s)
    print("Sending: " + phrase)
    queue = [sound[c] for c in phrase]
    out = startcode
    for char in queue:
        out += char
    play(out)
    print("Sent!")
    print("")

print("")
print("Duck Code V1.0 by Alex Davenport")
print("--------------------------------")
print("Type /quit to exit")
print("")

while 1:
    to_morse(input("Message to Send: "))
