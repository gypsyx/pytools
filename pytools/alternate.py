import sys

def is_alternate(istring):
    ''' Checks if the string is a sequence of two alternating
    characters
    '''
    if istring is None or len(istring) < 2: return False

    first = istring[0]
    sec = istring[1]

    if first == sec: return False

    for i, char in enumerate(istring):
        if i % 2 == 0 and char != first:
            return False
        elif i % 2 == 1 and char != sec:
            return False
        else:
            pass # don't care.
    return True




if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: alternate.py <string>")
        sys.exit(0)

    s = sys.argv[1]
    print(is_alternate(s))
