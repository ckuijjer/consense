import sys, json

#Read data from stdin
def read_in():
    lines = sys.stdin.read()
    #Since our input would only be having one line, parse our JSON data from that
    # print lines
    # print json.loads(lines)
    return json.loads(lines)
    # return lines

def main():
    #get our data as an array from read_in()
    lines = read_in()

    # print(lines["mySecretMessage"])

    reverted_string = lines["mySecretMessage"][::-1]

    sys.stdout.write(reverted_string)

#start process
if __name__ == '__main__':
    main()