import gl

def loadInitials():
    global initials
    file = open("data/initials.txt", "r", encoding= 'utf-8')
    count = 0
    for line in file:
        count = count + 1
        arr = line.split("\t")
        tmp = {'code': arr[0].strip(),'name':arr[1].strip(), 'comments':arr[2].strip()}
        gl.initials.append(tmp);
        #print(tmp)
    print("[Initials] Loaded "+str(count)+" entries.")

def loadFinals():
    global finals
    file = open("data/finals.txt", "r", encoding= 'utf-8')
    count = 0
    for line in file:
        count = count + 1
        arr = line.split("\t")
        tmp = {'code': arr[0].strip(),'name':arr[1].strip(), 'comments':arr[2].strip()}
        gl.finals.append(tmp);
        #print(tmp)
    print("[Finals] Loaded "+str(count)+" entries.")

def loadTones():
    global tones
    file = open("data/tones.txt", "r", encoding= 'utf-8')
    count = 0
    for line in file:
        count = count + 1
        arr = line.split("\t")
        tmp = {'code': arr[0].strip(),'name':arr[1].strip(), 'open':arr[2].strip()}
        gl.tones.append(tmp)
        #print(tmp)
    print("[Tones] Loaded "+str(count)+" entries.")

def loadAlphabets():
    global tones
    file = open("data/alphabets.txt", "r", encoding= 'utf-8')
    count = 0
    for line in file:
        count = count + 1
        arr = line.split("\t")
        tmp = {'code': arr[0].strip(),'name':arr[1].strip()}
        gl.alphabets.append(tmp)
        #print(tmp)
    print("[Alphabets] Loaded "+str(count)+" entries.")