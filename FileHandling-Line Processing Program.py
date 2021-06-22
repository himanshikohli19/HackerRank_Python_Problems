'''
WAP with function name filterFile makes a copy of oldfile,
omitting(excluding) any lines with begins with #.
'''

def filterFile(oldFile,newFile):
    f1=open(oldFile,"r")
    f2=open(newFile,"w")
    while True:
        text=f1.readline()
        if text=="":
            break
        if text[0]=="#":
            continue
        else:
            f2.write(text)
    f1.close()
    f2.close()
    return


oldFile = input("Enter name of an already created File: ")
newFile = input("Enter name of an newly created File: ")
filterFile(oldFile,newFile)
