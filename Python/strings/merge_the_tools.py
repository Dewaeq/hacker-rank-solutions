def merge_the_tools(string, k):
    n = len(string)
    l = list()
    for i in range(0, n, k):
        seen = set()
        s = "".join([x for x in string[i:i+k] if not(x in seen or seen.add(x))])
        l.append(s)
    print('\n'.join(l))


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
