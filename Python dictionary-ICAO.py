import re
from gtts import gTTS

d = {'a': 'alfa', 'b': 'bravo', 'c': 'charlie', 'd': 'delta', 'e': 'echo', 'f': 'foxtrot',
     'g': 'golf', 'h': 'hotel', 'i': 'india', 'j': 'juliett', 'k': 'kilo', 'l': 'lima',
     'm': 'mike', 'n': 'november', 'o': 'oscar', 'p': 'papa', 'q': 'quebec', 'r': 'romeo',
     's': 'sierra', 't': 'tango', 'u': 'uniform', 'v': 'victor', 'w': 'whiskey',
     'x': 'x-ray', 'y': 'yankee', 'z': 'zulu'}


def stringToICAO(name):
    listStr = []
    for x in name:
        listStr.append(d[x])
    return listStr


name = "Hosna Kalantar"
orgText = "Original Text"
convText = "Converted text"

x = name.lower()
x = re.sub('\s+', '', x)
dictList = str(stringToICAO(x))
dict = str(dictList)[1:-1]
text = orgText + " " + name, " " + convText + " " + dict
print(text)
myobj = gTTS(text=str(text), lang='en')
myobj.save("audio.mp3")
