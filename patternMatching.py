import random
import string
from typing import Tuple
from benchmark import benchmark

NUM_BENCH_ITER = 50
SIZE_BENCH_S1 = 500_000
SIZE_BENCH_S2 = 20_000


def match_bf(s1: str, s2:str) -> Tuple[int, Tuple[int, int]]:
    s2_len = len(s2)
    num_iter = 0 
    # Previous assignment.
    num_inst = 1
    
    for idx, c in enumerate(s1):
        num_iter += 1
        # Assignments (idx, c) + comparison + increment 
        # + following comparison.
        num_inst += 6

        if c == s2[0]:
            # Following addition and charwise comparison.
            num_iter += s2_len
            num_inst += 1 + s2_len

            if s1[idx : idx + s2_len] == s2:
                return (idx, (num_iter, num_inst))
        
    return (-1, (num_iter, num_inst))


def match_rabin_karp(s1: str, s2: str) -> Tuple[int, Tuple[int, int]]:
    s2_hash = hash(s2)
    s2_len = len(s2)
    num_iter = 0
    # Previous two assignments.
    num_inst = 2
    
    for idx in range(len(s1)):
        num_iter += 1
        # Assignments (idx, c) + comparison + increment 
        # + following assignment and hash O(n).
        num_inst += 6 + s2_len
        
        if hash(s1[idx : idx + s2_len]) == s2_hash:
            return (idx, (num_iter, num_inst))
    
    return (-1, (num_iter, num_inst))


def gen_str(size):
    return ''.join(random.choice(string.ascii_uppercase) for _ in range(size))


def main():
    for i in range(NUM_BENCH_ITER):
        s1 = gen_str(SIZE_BENCH_S1)
        s2 = gen_str(SIZE_BENCH_S2)
        res = []
        res.append(benchmark(match_bf, False, True, s1, s2))
        res.append(benchmark(match_rabin_karp, False, True, s1, s2))

        if (res[1:] != res[:-1]):
            print('error: conflicting results')
            return

        if res[0] != -1:
            print (f'found at {res[0]}\n')
        else:
            print('not found\n')


if __name__ == '__main__':
    main()
    