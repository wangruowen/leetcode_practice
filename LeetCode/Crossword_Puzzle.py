# https://www.hackerrank.com/challenges/crossword-puzzle/problem
# !/bin/python

import sys


def fill_words(crossword, words_position, rest_hints):
    if len(words_position) == 0 and len(rest_hints) == 0:
        return True

    for i in range(len(words_position)):
        word_start, word_end = words_position[i]
        if word_start[0] == word_end[0]:
            is_horizontal = True
            word_len = abs(word_start[1] - word_end[1]) + 1
        else:
            is_horizontal = False
            word_len = abs(word_start[0] - word_end[0]) + 1

        # print("start: (%d, %d) end (%d, %d) len %d is_horizontal = %d" % (word_start[0], word_start[1], word_end[0], word_end[1], word_len, sum([is_horizontal])))

        for j in range(len(rest_hints)):
            hint = rest_hints[j]
            if len(hint) == word_len:
                # print("hint: %s match length" % hint)
                filled_cells = []
                fill_fail = False
                if is_horizontal:
                    for k in range(word_start[1], word_end[1] + 1):
                        if crossword[word_start[0]][k] != "-":
                            # cur cell is already filled
                            if crossword[word_start[0]][k] != hint[k - word_start[1]]:
                                # conflict with existing letter
                                fill_fail = True
                                break
                        else:
                            # fill it and record
                            crossword[word_start[0]][k] = hint[k - word_start[1]]
                            filled_cells.append([word_start[0], k])
                            # print("fill cell: (%d, %d)" % (word_start[0], k))
                else:
                    for k in range(word_start[0], word_end[0] + 1):
                        if crossword[k][word_start[1]] != "-":
                            # cur cell is already filled
                            if crossword[k][word_start[1]] != hint[k - word_start[0]]:
                                # conflict with existing letter
                                fill_fail = True
                                break
                        else:
                            # fill it and record
                            crossword[k][word_start[1]] = hint[k - word_start[0]]
                            filled_cells.append([k, word_start[1]])
                            # print("fill cell: (%d, %d)" % (word_start[0], k))
                if fill_fail:
                    # rollback and try next
                    for i, j in filled_cells:
                        crossword[i][j] = "-"
                else:
                    # recursive
                    new_rest_hints = rest_hints[:j] + rest_hints[j + 1:]
                    new_word_positions = words_position[:i] + words_position[i + 1:]
                    if fill_words(crossword, new_word_positions, new_rest_hints):
                        return True
                    else:
                        # also rollback
                        for i, j in filled_cells:
                            crossword[i][j] = "-"
    return False


def crosswordPuzzle(crossword, hints):
    # Complete this function
    row_len, col_len = len(crossword), len(crossword[0])
    words_position = []
    # First, check row by row
    for i in range(row_len):
        start, end = None, None
        for j in range(col_len):
            if crossword[i][j] == "-":
                if not start:
                    start = (i, j)
                end = (i, j)
            elif start and end:
                if end[1] > start[1]:
                    words_position.append([start, end])
                start, end = None, None
        if start and end and end[1] > start[1]:
            words_position.append([start, end])
    # Second, check col by col
    for j in range(col_len):
        start, end = None, None
        for i in range(row_len):
            if crossword[i][j] == "-":
                if not start:
                    start = (i, j)
                end = (i, j)
            elif start and end:
                if end[0] > start[0]:
                    words_position.append([start, end])
                start, end = None, None
        if start and end and end[0] > start[0]:
            words_position.append([start, end])
    # print(words_position)
    # Backtracking
    hints_array = hints.split(";")
    # Change crossword to list of list
    crossword_array = []
    for each_line in crossword:
        crossword_array.append(list(each_line))
    # print(crossword_array)
    fill_words(crossword_array, words_position, hints_array)

    return ["".join(x) for x in crossword_array]


if __name__ == "__main__":
    crossword = []
    crossword_i = 0
    for crossword_i in xrange(10):
        crossword_t = str(raw_input().strip())
        crossword.append(crossword_t)
    hints = raw_input().strip()
    result = crosswordPuzzle(crossword, hints)
    print "\n".join(map(str, result))


