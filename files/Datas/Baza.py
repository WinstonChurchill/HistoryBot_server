import json
import codecs
from pprint import pprint

txt = []

with codecs.open('HelpFiles.txt', 'r', "utf_8_sig") as f:
    for i in f:
        i = i.replace('\n', '')
        i = i.replace('\r', '')
        txt.append(i.split(' – '))

txt1 = {}

for i in txt:
    txt1[i[0]] = i[1]

a = input()

with open('Data3v.json', 'a+') as f:
    data = json.load(f)
    print(data)
    #json.dump(data, f, sort_keys=True, indent=4)