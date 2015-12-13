# -*- coding: utf-8 -*-
import gl
import db
import load
import alphabet_IPA
#print('\u02e8')
#Drop all collections
db.clearDB()
#Import Initials
load.loadInitials()
db.buildInitialsDB()
#Import Finals
load.loadFinals()
db.buildFinalsDB()
#Import Tones
load.loadTones()
db.buildTonesDB()
#Import Alphabet Types
load.loadAlphabets()
db.buildAlphabetsDB()

print(alphabet_IPA.getSpelling('1','B1', '3'))
print(alphabet_IPA.getSpelling('1','B1', '2'))
