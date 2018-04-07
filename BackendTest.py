import sys, json

#Read data from stdin
def read_in():
    lines = sys.stdin.readlines()
    #Since our input would only be having one line, parse our JSON data from that
    return json.loads(lines[0])

def main():
    #get our data as an array from read_in()
    lines = read_in()

    reverted_string = lines[::-1]

    #return the sum to the output stream
    print reverted_string

#start process
if __name__ == '__main__':
    main()