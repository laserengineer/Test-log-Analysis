import re

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
    """
        Process Test log file and return only interested lines
        Args:
            fname_in, the input test log file name
            fname_out, the processed test log file name
        Returns:
            Processed test log txt file named as "fname_out"
    """

    with open(fname_in,'r') as rf:
        with open (fname_out,'w') as wf:
            for line in rf:
                if all(x in line for x in get_keys()[:]):
                    # if all the keys in the line`
                    wf.write(line)

def TestDataExact(fname_in,fname_out,min,max):
    """
        Only get the interested number from processed test log min < range < max
        return data only file
        Args:
            fname_in, the processed test log
            fname_out, the test data only text file
            min, minimum RTD value
            max, maximum RTD value
        Returns:
            fname_out, the processed test log file name
    """
    with open(fname_in,'r') as rf:
        with open (fname_out,'w') as wf:
            for line in rf:
                datalist = re.findall(r"[-+]?\d*\.\d+|\d+", line)
                if min < float(datalist[-4]) < max:
                    data = ','.join(datalist[-4:])
                    wf.write(data)
                    wf.write('\n')

TestLogProcess("Test Log.txt","Test log_1_Processed.txt")
TestDataExact("Test log_1_Processed.txt", 'Test Data_1.txt', 10, 500)

