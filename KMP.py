from z_algo import get_z, naive_impl
from readfile import read_reference_file, pattern_generator
import re
def get_sp(s):
    sp = [0]*len(s)
    z_list = get_z(s)
    for i in range(len(s)-1,0,-1):
        j = i + z_list[i] - 1
        sp[j] = z_list[i]
    check_splist(s, sp)
    return sp
def kmp(p, t):
    match = []
    sp_list = get_sp(p)
    j = 0
    while j <= len(t) - len(p):

        i = 0
        while i < len(p):
            if p[i] != t[i+j]:
                break
            i += 1
        if i == len(p):
            match.append(j)
            # print(j)
            jump_length = len(p) - sp_list[len(p)-1]
            # print(jump_length)
        else:
            jump_length = i - sp_list[i-1]

        jump_length = max(jump_length,1)
        j += jump_length
    return match
def check_splist(p, sp):
    for i in range(len(p)):
        assert p[:sp[i]]==p[i+1-sp[i]:i+1]
def check(text, pattern_gen):
    for i,pattern in enumerate(pattern_gen):
        kmp_result = kmp(pattern, text)
        n_result = naive_impl(pattern, text)
        if len(kmp_result) != len(n_result):
            print(kmp_result)
            print(n_result)
            print(len(kmp_result),len(n_result),i, pattern)
            break
        else:
            print(i)
    else:
        print('all correct')
if __name__ == '__main__':

    pattern_path = 'pattern-collection_2.txt'

    pattern_gen = pattern_generator(pattern_path)
    text = read_reference_file()
    # p = next(pattern_gen)
    # kmp(p, text)
    # check(text, pattern_gen)


    # for p in pattern_gen:
    #     t = text
    #     a = re.finditer(p, t)
    #     l = []
    #     for i in a:
    #         l.append(i.span(0)[0])
    #     nai = naive_impl(p, t)
    #     print(len(l), len(nai))
    #     assert len(l) == len(nai)


# 38147
# 39562, 38151
