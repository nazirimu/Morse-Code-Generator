# MORSE CODE PROJECT

# Imports
import os
import time

## INPUT TEXT
message = input('Please enter a message: \n')

## PROCESS TEXT

### NOTE: '0' - DOT, '1' - DASH - ALSO Numbers and special letters were excluded for timesake
MORSE_CODE = {
    'a': [0,1],
    'b': [1,0,0,0],
    'c': [1,0,1,0],
    'd': [1,0,0],
    'e': [0],
    'f': [0,0,1],
    'g': [1,1,0],
    'h': [0,0,0,0],
    'i': [0,0],
    'j': [0,1,1,1],
    'k': [1,0,1],
    'l': [0,1,0,0],
    'm': [1,1],
    'n': [1,0],
    'o': [1,1,1],
    'p': [0,1,1,0],
    'q': [1,1,0,1],
    'r': [0,1,0],
    's': [0,0,0],
    't': [1],
    'u': [0,0,1],
    'v': [0,0,0,1],
    'w': [0,1,1],
    'x': [1,0,0,1],
    'y': [1,0,1,1],
    'z': [1,1,0,0],
    ' ': '/'
}


message_array = list(message.lower())

message_in_morse = []
for letter in message_array:
    message_in_morse.append(MORSE_CODE[f'{letter}'])
    for item in MORSE_CODE[f'{letter}']:
        time.sleep(0.6)
        if item == 0:
            os.system("afplay dot.wav&")
            print('.', end=' ')

        elif item == 1:
            os.system("afplay dash.wav&")
            print('_', end=' ')

        else:
            print(' ', end=' ')
            time.sleep(0.2)
