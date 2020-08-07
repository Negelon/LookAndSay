from itertools import groupby
import sys

def look_and_say(n):
    return int(''.join(str(len(list(j))) + i for i, j in groupby(str(n))))


if __name__ == "__main__":
    args = sys.argv
    top = int(args[1])
    length = int(args[2])

    print(1, ':', top)

    result = None
    temp = None
    for i in range(0, length - 1):
        if result is None:
            temp = look_and_say(top)
            result = temp
        else:
            result = look_and_say(temp)
            temp = result
        print(f'{i + 2} : {result}')