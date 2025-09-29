# lab2-2_starter.py

LOGFILE = "sample_auth_small.log"  # change filename if needed

count = 0
List_ips =[]
Unique_List_Ips =[]

def simple_parser(line):
    """
    looks for the substring ' port ' and returns the following port number.
    Returns None if no matching substring found.
    """
    if " from " in line:
        parts = line.split() # splits the line into tokens, seperates by spaces by default
        try:
            anchor = parts.index("from")    # Find the position of the token "port", our anchor
            port = parts[anchor+1]          # the port value will be next token, anchor+1
            List_ips.append(port.strip())             # strip any trailing punctuation

        except (ValueError, IndexError):
            return None

    return None

## This is the main block that will run first. 
## It will call any functions from above that we might need.
if __name__ == "__main__":

    with open(LOGFILE, "r") as f:
        for line in f:
            (simple_parser(line.strip()))
            count +=1
    Unique_List_Ips=set(List_ips)
    Sorted_List_Ips=sorted(Unique_List_Ips)
    print("Total lines read: ",count)
    print("Number of Unique IPs: ",len(Unique_List_Ips))
    print("First 10 Unique Ips: ",Sorted_List_Ips[0:10])
    