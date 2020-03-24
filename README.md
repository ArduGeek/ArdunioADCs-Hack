# ArdunioADCs-Hack

simple solution for translating python generated wave form to PWM values for Arduino, and converting Arduino analog input values to wave files

![Arduino](/mnt/mmc-SD64G_0xdabeab8b/SCHOOL/PrezentacjaKonferencja/arduino.jpg)

## Table of contents:
1. In what projects you can use this tool?
2. What are the parts of this tool?
3. Parts of tools explained
4. How to use this tool?
6. To do list
5. Conclusion


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
2. reads contents of the file and assigns them to variable named *string*
3. closes the file named text

```python
sampleRate = 44100.0
duration = 100.0
frequency = 440.0
```
here i just assign parameters of wave file

```python
obj = wave.open('sound_writer.wav','w')
obj.setnchannels(1) # mono
obj.setsampwidth(2)
obj.setframerate(sampleRate)
```
1. Script opens file called sound_writer.wav with permission to write in it and assigns under variable *obj*
2. number of channels in file is defined
3. length of single sample is defined
4. "framerate" of audio file is defined, which is assigned in *sampleRate* variable
```python
audio=[]
audio = string.splitlines()
audio2 = []
```
1. *audio* list is created
2. we invoke splitlines() method on *string* variable which split it in lines and assigns it to variable *audio*
3. *audio2* list in created
```python
for i in audio:
	audio2.append(int(i))
print(audio2)
```
1. for loop in *audio* variable is invoked inside this method we convert *i* variable to integer
2. then we print *audio* variable
```python
for c in audio2:
	data = struct.pack('<h', c)
	obj.writeframesraw( data )
obj.close()
```
1. we use for loop to iterate through *audio2* list
2. we use struct.pack() function to sign values to *data* variable, basically makes empty space suitable for writing .wav data 
3. then we write frames of data to our empty object with name *data*
4. we close the .wav file

###### this is whole mechanism of how this thing works, it can be used to write anything to audio file unless it is in values.txt file and it is in range of +/- 32768

#### translate_to_pwm.py
whole code of the script
```python
import numpy as np

text = open("./pwm.txt")
string = text.read()
text.close()
lines = string.splitlines()
values = []
result = []
counter = 0
for i in lines:
	values.append(float(i))	
for i in values:
	counter += 1
	result.append(int(round(np.interp
	(i,[-1,1],[0,255]),0)))
print(result)
```
```python
text = open("./pwm.txt")
string = text.read()
text.close()
lines = string.splitlines()
values = []
result = []
counter = 0
```
1. script opens pwm.txt file and saves it under *text* variable
2. file assigned under *text* variable is read and result of that is saved under *string* variable
3. then *file* is closed
4. then we split *string* variable in lines
5. list *values* is created
6. list *result* is created
7. integer *counter* is created

```python
for i in lines:
	values.append(float(i))
```
in this loop we go through values in list *lines* and append them to list *values* after converting them to to float type
```python
for i in values:
	counter += 1
	result.append(int(round(np.interp
	(i,[-1,1],[0,255]),0)))
print(result)
```
in this loop we go through data in list *values*, we add one to variable *counter* that was not used anywhere, we append value of variable *i* converted to integer rounded so it doesn't have decimal points and interpolate it from ramge of -1, 1 to 0, 255 and then we print result
###### that's everything you should know about this tool, it can be used to convert any value to PWM duty cycle value. Down there is little example how to calculate sine wave values for pwm.txt file in order to convert them to pwm
```python
Python 3.6.9 (default, Nov  7 2019, 10:44:02) 
[GCC 8.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import math as mth
>>> import numpy as np
>>> range = np.arange(0,6.28,0.01)
>>> result = []
>>> for i in range:
...     result.append(mth.sin(i))
... 
>>> print(result)
[0.0, 0.009999833334166664, 0.01999866669333308, 0.02999550020249566, 0.03998933418663416, 0.04997916927067833, 0.059964006479444595, 0.06994284733753277, 0.0799146939691727, 0.08987854919801104, 0.09983341664682815, 0.10977830083717481, 0.11971220728891936, 0.12963414261969486, 0.1395431146442365, 0.14943813247359922, 0.15931820661424598, 0.16918234906699603, 0.17902957342582418, 0.18885889497650057, 0.19866933079506122, 0.20845989984609956, 0.21822962308086932, 0.2279775235351884, 0.23770262642713458, 0.24740395925452294, 0.2570805518921551, 0.26673143668883115, 0.27635564856411376, 0.28595222510483553, 0.29552020666133955, 0.3050586364434435, # and it goes on ... forever ...
```
###### Try to experiment with different step values (last value in np.arange() function), e.g. 0.1; 0.5; 1. And see how quality of wave will change after interpolating them to +/- 32768 range and writing them with wave_file_writer.py to file

#### trans_ard_wav.py

###### To be continued

### To do list

- [x] translate from python to pwm cycle
- [x] translate from arduino analog input to wave file
- [ ] generate simple wave forms in .wav files 
- [ ] translate from arduino analog input to matplotlib
- [ ] make GUI for whole project
- [ ] make text/GUI based simple tone .wav file generator
- [ ] ascii to digital signal converter in .wav and arduino

if have more ideas for interesting improvements for this project please contact me, or just submit change.

### Conclusion
In my opinion it was interesting project. This project can learn you a bit about digital signal processing .wav files and a bit about arduino. If you have some more spare time and you wan to see videos explaining similar projects to this one you can visit my [website](http://www.ardugeek.pl)
