#Caleb Mayer
#CSCI 102
#week 12 part A and B

def PrintOutput(beans):
    print('OUTPUT',beans)

def LoadFile(fileboi):
    intake = open(fileboi,'r')
    out = []
    for lines in intake:
        out.append(lines.replace('\n',''))
    return(out)
def UpdateString(stronk,replonk,place):
    listboi = [i for i in stronk]
    listboi[place] = replonk
    out = ''.join(listboi)
    print(out)
def FindWordCount(listicate,what):
    output = listicate.count(what)
    return(output)
players = ["Mary", "Cody", "Joe", "Jill", "Xai", "Bodo"]
scores = [5, 8, 10, 6, 10, 4]
players2 = ["Melvin", "Martian", "Baka", "Xai", "Cody"]
def ScoreFinder(child,numbers,whomst):
    childs = [i.lower() for i in list(child)]
    if whomst.lower() in childs:
        print('OUTPUT',child[childs.index(whomst.lower())],'got a score of',numbers[childs.index(whomst.lower())])
    else:
        print('OUTPUT Player not found')

def Union(thing,otherthing):
    out = thing
    for things in otherthing:
        if things not in thing:
            out.append(things)
    return(out)
print("OUTPUT", Union(scores, players2))