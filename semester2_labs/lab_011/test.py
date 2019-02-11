import sys

def contains(chars, s):
    for c in chars:
        if c in s:
            s = s.replace(c, '', 1)
        else:
            return False
    return True

def main():
    for line in sys.stdin:
        [chars, s] = line.lower().split().strip()
        print(contains(chars, s)



if __name__ == '__main__':
    main()
