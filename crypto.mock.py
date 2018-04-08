import sys, json

def read_in():
    lines = sys.stdin.read()

    return json.loads(lines)

def main():
    lines = read_in()
    
    output = 0

    if int(lines["age"]) == 18:
       output = 1500
    else:    
       output = 1

    sys.stdout.write(str(output))


if __name__ == '__main__':
    main()