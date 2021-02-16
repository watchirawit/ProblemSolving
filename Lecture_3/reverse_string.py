"""
def reverse_for_loop(s):
    sl = ''
    for c in s:
        sl = c + sl
    return sl

input_str = 'INE-KMUTNB'

if __name__ == "__main__":
    print('Reverse String using for_loop =',reverse_for_loop(input_str))

def reverse_slicing(s):
    return s[::-1]

input_str = 'INE-KMUTNB'

if __name__ == "__main__":
    print('Reverse String using slicing =',reverse_slicing(input_str))




def reverse_while_loop(s):
    sl = ''
    length = len(s) - 1
    while length >= 0:
        sl = sl + s[length]
        length -= 1
    return sl

input_str = 'INE-KMUTNB'

if __name__ == "__main__":
    print('Reverse String using while_loop =',reverse_while_loop(input_str))
"""

def reverse_str_join(s):
    sl = ''.join(reversed(s))
    return sl

input_str = 'INE-KMUTNB'

if __name__ == "__main__":
    print('Reverse String using str_join =',reverse_str_join(input_str))