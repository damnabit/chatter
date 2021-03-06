#!/usr/bin/env python

# Copyright 2010, 2014 Kevin Reid
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

import os, random, time

voices = [
   "Agnes",
   "Albert",
   "Alex",
   "Alice",
   "Alva",
   "Amelie",
   "Anna",
   "Bad",
   "Bahh",
   "Bells",
   "Boing",
   "Bruce",
   "Bubbles",
   "Carmit",
   "Cellos",
   "Damayanti",
   "Daniel",
   "Deranged",
   "Diego",
   "Ellen",
   "Fiona",
   "Fred",
   "Good",
   "Hysterical",
   "Ioana",
   "Joana",
   "Junior",
   "Kanya",
   "Karen",
   "Kathy",
   "Kyoko",
   "Laura",
   "Lekha",
   "Luciana",
   "Mariska",
   "Mei-Jia",
   "Melina",
   "Milena",
   "Moira",
   "Monica",
   "Nora",
   "Paulina",
   "Pipe",
   "Princess",
   "Ralph",
   "Samantha",
   "Sara",
   "Satu",
   "Sin-ji",
   "Tarik",
   "Tessa",
   "Thomas",
   "Ting-Ting",
   "Trinoids",
   "Veena",
   "Vicki",
   "Victoria",
   "Whisper",
   "Xander",
   "Yelda",
   "Yuna",
   "Zarvox",
   "Zosia",
   "Zuzana"
]

# TODO: Might want to omit some words / use a different list.
words = [x.rstrip().lower() for x in open("/usr/share/dict/words")]

words_per_word = 4
words_per_voice = 5

# For information on these commands, see Apple's Speech Synthesis Programming Guide.
# https://developer.apple.com/library/mac/documentation/UserExperience/Conceptual/SpeechSynthesisProgrammingGuide/FineTuning/FineTuning.html#//apple_ref/doc/uid/TP40004365-CH5-SW10
commands = "[[rate 1]][[volm 0.1]]"

while True:
    voice = random.choice(voices)
    text = " ".join(" ".join(random.sample(words, words_per_word)) for _ in xrange(words_per_voice))
    print voice, "-", text
    os.spawnlp(os.P_NOWAIT, "say", "say", "-v", voice, commands, text)
    time.sleep(10)
