import codecs
import random

import numpy as np
import pyperclip

emojis = {
    '0': ":zero:",
    '1': ":one:",
    '2': ":two:",
    '3': ":three:",
    '4': ":four:",
    '5': ":five:",
    '6': ":six:",
    '7': ":seven:",
    '8': ":eight:",
    '9': ":nine:",
    'x': ":bomb:"
}


def initBoard(size, mine_count):
    b = np.chararray([size, size])
    mines = 0
    for i in range(size):
        for j in range(size):
            b[i][j] = '0'
    while mines < mine_count:
        for i in range(size):
            for j in range(size):
                if random.randint(0, 5) == 5 and mines < mine_count:
                    b[i][j] = 'x'
                    mines += 1
    return b


def checkForMines(b, size):
    for i in range(size):
        for j in range(size):
            if bytes.decode(b[i][j]) != 'x':
                count = 0
                for x in range(max(0, i - 1), min(size, i + 2)):
                    for y in range(max(0, j - 1), min(size, j + 2)):
                        if bytes.decode(b[x][y]) == 'x':
                            count += 1
                b[i][j] = codecs.encode(chr(ord(b[i][j]) + count))


def genDiscordBoard(b, size):
    new_b = []
    for i in range(size):
        row = []
        for j in range(size):
            row.append("||" + emojis[bytes.decode(b[i][j])] + "||")
        new_b.append(row)
    return new_b


if __name__ == "__main__":
    bsize = 8
    board = initBoard(bsize, 8)
    checkForMines(board, bsize)

    copytext = '\n'.join(''.join(row) for row in genDiscordBoard(board, bsize))
    pyperclip.copy(copytext)
