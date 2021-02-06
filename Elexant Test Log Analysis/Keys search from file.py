import re
"""
# Load file from keys.txt
keys = []
with open('keys.txt','r') as filehandle:
    filecontents = filehandle.readlines()

    for line in filecontents:
		#Only include the beginning tohe last 2 character, remove the line breaker

        current_place = line[:-1]
        keys.append(current_place)
"""

"""
# Process Test_Log file based on keys
with open('Test Log.txt', 'r') as rf:
    with open('Test Log_1_Processed.txt', 'w') as wf:
        for line in rf:
             if all(x in line for x in get_keys()[:]):
            #if all(x in keys[:] for x in line):
                wf.write(line)
"""


def get_keys():
    """
        Get all keys from keys.txt file

        Args:
            none, the function will read keys.txt file

        Returns:
            list[str]: List of keys
        """
    keys = []
    with open ('keys.txt','r') as keyfile:
        keycontents = keyfile.readlines()

        for line in keycontents:
            current_place = line [:-1] # the last string is line breaker that is not needed
            keys.append(current_place)
    return keys

def TestLogProcess(fname_in , fname_out):
    with open(fname_in,'r') as rf:
        with open (fname_out,'w') as wf:
            for line in rf:
                if all(x in line for x in get_keys()[:]):
                    # if all the keys in the line`
                    wf.write(line)

def TestDataExact(fname_in,fname_out,min,max):
    with open(fname_in,'r') as rf:
        with open (fname_out,'w') as wf:
            for line in rf:
                datalist = re.findall(r"[-+]?\d*\.\d+|\d+", line)
                if min < float(datalist[-4]) < max:
                    data = ','.join(datalist[-4:])
                    wf.write(data)
                    wf.write('\n')

TestLogProcess("Test Log.txt","Test log_1_Processed.txt")
TestDataExact("Test log_1_Processed.txt", 'Test Data_1.txt', 10, 100)

'''
with open ('Test log_1_Processed.txt','r') as rf:
    with open('Test Data_1.txt','w') as wf:
        for line in rf:
            datalist = re.findall(r"[-+]?\d*\.\d+|\d+", line)
            if 10< float(datalist[-4]) <500:
                data = ' '.join(datalist[-4:])
                wf.write(data)
                wf.write("\n")

'''

"""
# Process RTD2

keys = ['TS2','verification']

with open('Test Log.txt', 'r') as rf:
    with open('Test Log_2_Processed.txt', 'w') as wf:
        for line in rf:
            if all(x in line for x in keys[:]):
                wf.write(line)

with open ('Test log_2_Processed.txt','r') as rf:
    with open('Test Data_2.txt','w') as wf:
        for line in rf:
            datalist = re.findall(r"[-+]?\d*\.\d+|\d+", line)
            if 10< float(datalist[-4]) <500:
                data = ' '.join(datalist[-4:])
                wf.write(data)
                wf.write("\n")

# Process Limiter

keys = ['TS4','verification']

with open('Test Log.txt', 'r') as rf:
    with open('Test Log_4_Processed.txt', 'w') as wf:
        for line in rf:
            if all(x in line for x in keys[:]):
                wf.write(line)

with open ('Test log_4_Processed.txt','r') as rf:
    with open('Test Data_4.txt','w') as wf:
        for line in rf:
            datalist = re.findall(r"[-+]?\d*\.\d+|\d+", line)
            if 10< float(datalist[-4]) <500:
                data = ' '.join(datalist[-4:])
                wf.write(data)
                wf.write("\n")


"""
