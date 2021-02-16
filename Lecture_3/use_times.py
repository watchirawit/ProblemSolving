import timeit

def reverse_slicing(s):
    return s[::-1]

def reverse_for_loop(s):
    sl = ''
    for c in s:
        sl = c + sl
    return sl

def reverse_while_loop(s):
    sl = ''
    length = len(s) - 1
    while length >= 0:
        sl = sl + s[length]
        length -= 1
    return sl

def reverse_str_join(s):
    sl = ''.join(reversed(s))
    return sl

def reverse_list(s):
    temp_list = list(s)
    temp_list.reverse()
    return ''.join(temp_list)

def reverse_recursion(s):
    if len(s) == 0:
        return s
    else:
        return reverse_recursion(s[1:]) + s[0]

def slicing_time():
    SETUP = '''
from __main__ import reverse_slicing
'''
    TEST_CODE = '''
input_str = 'INE-KMUTNB'
reverse_slicing(input_str)
'''
    times = timeit.repeat(setup=SETUP,
                            stmt=TEST_CODE,
                            repeat=10,
                            number=100000)

   # print(times)
    print('Slicing time(millisecond): {}'.format(min(times)*1000))

def for_loop_time():
    SETUP = '''
from __main__ import reverse_for_loop
'''
    TEST_CODE = '''
input_str = 'INE-KMUTNB'
reverse_for_loop(input_str)
'''
    times = timeit.repeat(setup=SETUP,
                            stmt=TEST_CODE,
                            repeat=10,
                            number=100000)

    #print(times)
    print('for_loop_time(millisecond): {}'.format(min(times)*1000))

def while_loop_time():
    SETUP = '''
from __main__ import reverse_while_loop
'''
    TEST_CODE = '''
input_str = 'INE-KMUTNB'
reverse_while_loop(input_str)
'''
    times = timeit.repeat(setup=SETUP,
                            stmt=TEST_CODE,
                            repeat=10,
                            number=100000)

   # print(times)
    print('while_loop_time(millisecond): {}'.format(min(times)*1000))

def str_join_time():
    SETUP = '''
from __main__ import reverse_str_join
'''
    TEST_CODE = '''
input_str = 'INE-KMUTNB'
reverse_str_join(input_str)
'''
    times = timeit.repeat(setup=SETUP,
                            stmt=TEST_CODE,
                            repeat=10,
                            number=100000)

   # print(times)
    print('str_join_time(millisecond): {}'.format(min(times)*1000))

def list_time():
    SETUP = '''
from __main__ import reverse_list
'''
    TEST_CODE = '''
input_str = 'INE-KMUTNB'
reverse_list(input_str)
'''
    times = timeit.repeat(setup=SETUP,
                            stmt=TEST_CODE,
                            repeat=10,
                            number=100000)

   # print(times)
    print('list_time(millisecond): {}'.format(min(times)*1000))

def recursion_time():
    SETUP = '''
from __main__ import reverse_recursion
'''
    TEST_CODE = '''
input_str = 'INE-KMUTNB'
reverse_recursion(input_str)
'''
    times = timeit.repeat(setup=SETUP,
                            stmt=TEST_CODE,
                            repeat=10,
                            number=100000)

   # print(times)
    print('recursion_time(millisecond): {}'.format(min(times)*1000))

if __name__ == '__main__':
    slicing_time()
    for_loop_time()
    while_loop_time()
    str_join_time()
    list_time()
    recursion_time()