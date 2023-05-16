from benchmark import benchmark
import random
import string

NUM_BENCH_ITER = 10
SIZE_BENCH_S1 = 500_000_000
SIZE_BENCH_S2 = 10


import string
def KMPSearch(pat, txt):
    M = len(pat)
    N = len(txt)

    # cria lps[] que vai guardar o maior
    # valor prefixo sufixo para o padrão
    lps = [0]*M
    j = 0 # index for pat[]

    # Calcula lps[]
    computeLPSArray(pat, M, lps)
    print (lps)

    i = 0 # index for txt[]
    while (i < N):
        if (pat[j] == txt[i]):
            j += 1
            i += 1

        if (j == M):
            print("Found pattern at index "+str(i - j))
            print("pat=",pat,"txt=",txt[i-j:i-j+M])
            j = lps[j - 1]

        elif (i < N and pat[j] != txt[i]):
            # Não faz match dos caracteres lps[0..lps[j-1]],
            # não é necesssário, eles combinarão
            if (j != 0):
                j = lps[j - 1]
            else:
                i += 1


def computeLPSArray(pat, M, lps):
    # tamanho do maior prefixo sufixo anterior
    len = 0
    i = 1
    lps[0] = 0 # lps[0] is always 0

    # loop calcula lps[i] for i = 1 to M-1
    while (i < M):
        if (pat[i] == pat[len]):
            len += 1
            lps[i] = len
            i += 1
        else: # (pat[i] != pat[len])
            if (len != 0):
                len = lps[len - 1]
            else: # if (len == 0)
                lps[i] = len
                i += 1
      
        
def gen_str(size):
    return ''.join(random.choice(string.ascii_uppercase) for _ in range(size))


def main():
    #s1 = gen_str(SIZE_BENCH_S1)
    #s2 = gen_str(SIZE_BENCH_S2)
    
    s1 = "AAAAAAAAAAA"
    s2 = "AAABBAAA"

    KMPSearch(s2,s1)

            
if __name__ == "__main__":
    main()