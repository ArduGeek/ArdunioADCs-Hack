# ArdunioADCs-Hack

simple solution for translating python generated wave form to PWM values for Arduino, and converting Arduino analog input values to wave files

## Table of contents:
1. In what projects you can use this tool?
2. What are the parts of this tool?
3. Parts of tools explained
4. How to use this tool?

### Where you can use this tool?
I made this set of tools because i thought that, it would be interesting to record wave forms with Arduino analog inputs and then use e.g. audacity to edit and inspect the recorded waveform with e.g. FFT. It can also be used to record readings from a sensor, you can leave raspberry pi with simple PyFirmata script reading values and writing them to text file, than after longer amount of time toy can get back copy the file put it into my script which converts it and then plot it or save in wave file.

### Parts of this tool.
This tool is made out of few parts:
* values.txt
	* in this file you paste in values for wave_file_writer.py, they should be in range od -32768, 32768
* input.txt
	* in this file you paste or write values read by arduino ADC they should be in range of 0, 1024
* pwm.txt
	* this is the file in which you put values for translate_to_pwm.py they should be in range of -1, 1
* wave_file_writer.py
	* this script is used to as the name applies write data from values.txt to .wav file
* translate_to_pwm.py
	* this script converts vales from range -1, 1 to 0, 255, which are the values for arduino pwm output
* trans_ard_wav.py
	*this file takes arduino analog input values in range of 0, 1024 and converts them to values of 16 bit depth .wav file

### Parts explained
#### wave_file_writer.py

whole code of the script

```python
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
```

```python
text = open("./values.txt") 
string = text.read()
text.close()
```
1. script opens file in current directory named values.txt
2. reads contents of the file and assigns them to variable named string
3. closes the file named text

```python
sampleRate = 44100.0
duration = 100.0
frequency = 440.0
```
here i just assigned parameters of wave file

```python
obj = wave.open('sound_writer.wav','w')
obj.setnchannels(1) # mono
obj.setsampwidth(2)
obj.setframerate(sampleRate)
```
1. Script opens file called sound_writer.wav with permission to write in it and assigns under variable obj
2. number of channels in file is defined
3. length of single sample is defined
4. "framerate" of audio file is defined, which is assigned in sampleRate variable
```python
audio=[]
audio = string.splitlines()
audio2 = []
``` 
1. audio list is created
2. we invoke splitlines() method on string variable which split it in lines and assigns it to variable audio
3. audio2 list in created
```python
for i in audio:
	audio2.append(int(i))
print(audio2)
```
1. for loop in audio variable is invoked

#### translate_to_pwm.py

#### trans_ard_wav.py

# This markdown is still in progress
