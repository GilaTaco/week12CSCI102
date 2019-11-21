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
    print(out)
def UpdateString(stronk,replonk,place):
    listboi = [i for i in stronk]
    listboi[place] = replonk
    out = ''.join(listboi)
    print(out)
UpdateString("Hello World", "a", 3)