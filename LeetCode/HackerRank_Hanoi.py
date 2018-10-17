#!/bin/python3
# https://www.hackerrank.com/challenges/gena/problem

import math
import os
import random
import re
import sys
from collections import deque

done_state = None

def next_comb(comb):
    for i in range(len(comb)):
        if comb[i] != "":
            for j in range(len(comb)):
                if i == j: continue
                if comb[j] == "" or int(comb[j][0]) > int(comb[i][0]):
                    # comb[i][0] disc can be moved onto comb[j][0]
                    new_comb = comb[:]
                    new_comb[i] = comb[i][1:]
                    new_comb[j] = comb[i][0] + comb[j]
                    # order from 1 to 4 to reduce the search space
                    new_comb[1:] = sorted(new_comb[1:], key=lambda x: int(x[0]) if len(x) > 0 else -1)
                    yield new_comb

def is_done(comb):
    if comb[0] == done_state and "".join(comb[1:]) == "":
        return True
    return False
                    
def bfs(init_combin):
    queue = deque([[init_combin, 0]])
    visited_combins = set()        
    visited_combins.add(" ".join(init_combin))
    while len(queue) > 0:
        node = queue.popleft()
        cur_combin = node[0]        
        steps = node[1] + 1
        for new_combin in next_comb(cur_combin):
            if " ".join(new_combin) in visited_combins:
                continue
            if is_done(new_combin):
                return steps
            visited_combins.add(" ".join(new_combin))
            queue.append([new_combin, steps])
    
    return -1        

if __name__ == '__main__':
    N = int(input())
    done_state = "".join(map(str, range(N)))
    a = list(map(int, input().rstrip().split()))
    # Make it 0-based index as the initial combination of 4 rods
    init_combination = ["" for _ in range(4)] # 4 Rods, each is a string from small to large disc
    for disc_size, hanoi_index in enumerate(a):
        init_combination[hanoi_index-1] += str(disc_size)
    print(bfs(init_combination))

