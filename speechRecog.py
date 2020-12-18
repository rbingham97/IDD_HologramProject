#!/usr/bin/env python3

from vosk import Model, KaldiRecognizer
import sys
import os
import wave
import json
import serial
import time

ser = serial.Serial('/dev/ttyUSB0', 9600)

wf = wave.open(sys.argv[1], "rb")

model = Model("model")
rec = KaldiRecognizer(model, wf.getframerate(), "show video one two three")

while True:
	data = wf.readframes(4000)
	if len(data) == 0:
		break
	if rec.AcceptWaveform(data):
		print(rec.Result())
	else:
		print(rec.PartialResult())

message = bytes(str(json.loads(rec.FinalResult())['text']), 'ascii')
ser.write(message)

print("Done! Wrote to Serial: " + str(message))