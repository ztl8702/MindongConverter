# -*- coding: utf-8 -*-
import gl
import db

initials = {}
finals = {}
tones = {}

file = open("data/alphabets/IPA/initials.txt", 'r', encoding = 'utf-8')
for line in file:
    arr = line.split('\t')
    initials[arr[0].strip()]= arr[1].strip()
#Load IPA finals
file = open("data/alphabets/IPA/finals.txt", 'r', encoding = 'utf-8')
for line in file:
    arr = line.split('\t')
    finals[arr[0].strip()]= arr[1].strip()
#Load IPA tones
file = open("data/alphabets/IPA/tones.txt", 'r', encoding = 'utf-8')
for line in file:
    arr = line.split('\t')
    tones[arr[0].strip()]= arr[1].strip()
print("[Alphabet_IPA] Data loaded.")

def isOpen(toneCode):
    cursor = db.tones.find({'code':toneCode})
    for item in cursor:
        return item['open']
#print(tones)
def getSpelling(initialCode, finalCode, toneCode):
    result = ''
    if int(initialCode) in range(1,15):
        result = result + initials[initialCode]
    if finalCode[0] in ['A','B','C','D']:
        if finalCode[0]=='A':
            id = (int(finalCode[1:])-1)*2+1+(isOpen(toneCode))
        elif finalCode[0]=='B':
            id = (int(finalCode[1:])-1)*2+1+(isOpen(toneCode))+14
        elif finalCode[0]=='C':
            id = (int(finalCode[1:])-1)*2+1+(isOpen(toneCode))+38
        else:
            id = (int(finalCode[1:])-1)*2+1+(isOpen(toneCode))+62
        result = result + finals[str(id)]
    if int(toneCode) in range(1,7):
        result = result + tones[toneCode]
    return result