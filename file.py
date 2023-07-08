import os
os.chdir('/workspaces/cmagnon/HeadFirstPython/chapter3')

man = []
other = []

try:
    datafile = open('sketch.txt')

    for line in datafile:
        try:
            actor, saying = line.split(":", 1)
            saying = saying.strip()
            if actor == 'Man':
                man.append(saying)
            elif actor == 'Other Man':
                other.append(saying)
                
            #print(actor,end='')
            #print('Said:',end='')
            #print(saying,end='')
        except ValueError:
            pass

    datafile.close()
except IOError:
    print("File Not found: sketch.txt")

try:
    file_man = open("man_data.txt","w")
    file_other = open("other_data.txt","w")
    print(man,file=file_man)
    print(other,file=file_other)

except IOError:
    print("Files couln't be created. check OS.")
finally:
    file_man.close()
    file_other.close()