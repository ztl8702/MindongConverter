import gl
from pymongo import MongoClient
client = MongoClient()
db = client.mindong
initials = db.initials
finals = db.finals
tones = db.tones
alphabets = db.alphabets
spellings = db.spellings
syllables = db.syllables

def buildTonesDB():
    global tones
    for item in gl.tones:
        tones.insert_one(item)

def buildFinalsDB():
    global finals
    for item in gl.finals:
        finals.insert_one(item)

def buildInitialsDB():
    global initials
    for item in gl.initials:
        initials.insert_one(item)

def clearDB():
    db.drop_collection(finals)
    db.drop_collection(tones)
    db.drop_collection(initials)
    db.drop_collection(alphabets)
    db.drop_collection(spellings)
    db.drop_collection(syllables)
