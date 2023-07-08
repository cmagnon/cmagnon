import os
os.chdir('/workspaces/cmagnon/HeadFirstPython/chapter3')

man=[]
other=[]

try:
    with open("sketch.txt") as datafile:
        for line in datafile:
            try:
                actor, saying = line.split(":", 1)
                saying = saying.strip()
                if actor == 'Man':
                    man.append(saying)
                elif actor == 'Other Man':
                    other.append(saying)
            except ValueError:
                pass
    with open("man_data.txt", "w") as man_file:
        print(man, file=man_file)
    with open("other_data.txt", "w") as other_file:
        print(other,file=other_file)

except IOError as err:
    print("File Error: " + str(err))