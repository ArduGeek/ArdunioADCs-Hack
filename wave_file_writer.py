import wave, struct, math, random, numpy

text = open("./values.txt")
string = text.read()
text.close()

sampleRate = 44100.0
duration = 100.0
frequency = 440.0
obj = wave.open('sound_writer.wav','w')
obj.setnchannels(1) # mono
obj.setsampwidth(2)
obj.setframerate(sampleRate)
audio=[]
audio = string.splitlines()
audio2 = []
for i in audio:
	audio2.append(int(i))
print(audio2)
for c in audio2:
	data = struct.pack('<h', c)
	obj.writeframesraw( data )
obj.close()

