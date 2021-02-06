# File Objects
keys1 = ['TS1','verification']
keys = []
with open('keys.txt','r') as filehandle:
    filecontents = filehandle.readlines()

    for line in filecontents:
        current_place = line[:-2]

        keys.append(current_place)

print(keys,end='\n')
