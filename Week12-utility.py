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
