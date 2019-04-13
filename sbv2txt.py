
import sys

def isCaptionText(lineIndex):
    if lineIndex <= 0:
        return False

    # the text is on every third line starting from the second line
    return (lineIndex - 1)%3 == 0

if len(sys.argv) < 3:
    print('Arguments: [source sbv filename] [destination txt filename]')
    sys.exit()

with open(sys.argv[1]) as f1:
    with open(sys.argv[2], 'a') as f2:
        lines = f1.readlines()
        for index, line in enumerate(lines):
            if isCaptionText(index):
                f2.write(line)

print('Output complete. File written as ' + sys.argv[2])
