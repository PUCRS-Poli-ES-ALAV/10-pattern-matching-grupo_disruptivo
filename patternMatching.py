import random
import string
from typing import Tuple
from benchmark import benchmark


def patternMatching(s1: str, s2:str) -> Tuple[int, int]:
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
            num_inst += 1 + s2_len

            if s1[idx : idx + s2_len] == s2:
                return (idx, (num_iter, num_inst))
        
    return (-1, (num_iter, num_inst))


def stringGeneration(size):
    return ''.join(random.choice(string.ascii_uppercase) for _ in range(size))


def main(): 
    s1 = stringGeneration(100_000)
    s2 = stringGeneration(10)   
    index = benchmark(patternMatching, False, True, s1, s2)

    if index == -1:
        print (s2 + ' not found')
    else:
        print (s2  + ' found at index ' + str(index))


if __name__ == '__main__':
    main()
    