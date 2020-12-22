def swap_case(s):
    return s.swapcase()
    '''
    t = ""
    for x in s:
        for k in x:
            if k.isupper():
                t += k.lower()
            if k.islower():
                t += k.upper()
            elif not k.isalpha():
                t += k
    return t
    '''


if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
