import gl
import db
import load


load.loadInitials()
load.loadFinals()
load.loadTones()

#Import Initials, Finals and Tones into DB
db.clearDB()
db.buildInitialsDB()
db.buildFinalsDB()
db.buildTonesDB()
