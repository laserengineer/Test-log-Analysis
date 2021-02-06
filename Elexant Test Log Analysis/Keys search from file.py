import re

keys = []
with open('keys.txt','r') as filehandle:
    filecontents = filehandle.readlines()

    for line in filecontents:
		#Only include the beginning to the last 2 character, remove the line breaker

        current_place = line[:-1]
        keys.append(current_place)


with open('Test Log.txt', 'r') as rf:
    with open('Test Log_Processed.txt', 'w') as wf:
        for line in rf:
            if all(x in line for x in keys[:]):
                wf.write(line)

with open ('Test log_Processed.txt','r') as rf:
    with open('Test Data.txt','w') as wf:
        for line in rf:
            datalist = re.findall(r"[-+]?\d*\.\d+|\d+", line)
            data = ' '.join(datalist[-4:])
            wf.write(data)
            wf.write("\n")
