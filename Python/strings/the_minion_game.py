from itertools import combinations


def minion_game(string):
    n = len(string)
    score_kevin, score_stuart = 0, 0
    for i in range(n):
        if string[i].upper() in "AEIOU":
            score_kevin = score_kevin + n - i
        else:
            score_stuart = score_stuart + n - i
    if score_kevin > score_stuart:
        print("Kevin " + str(score_kevin))
    elif score_stuart > score_kevin:
        print("Stuart " + str(score_stuart))
    else:
        print("Draw")

    '''
    Not memory efficient and just stupid

    l = []
    for i in range(1, n+1):
        t = string[0:i]
        l.append(t)

        for j in range(i, n):
            k = string[i:(j+1)]
            l.append(k)

    kevin = [x for x in l if x[0] in 'AEIOU']
    stuart = [x for x in l if x not in kevin]

    score_kevin = sum([kevin.count(x) for x in set(kevin)])
    score_stuart = sum([stuart.count(x) for x in set(stuart)])

    if score_kevin > score_stuart:
        print("Kevin " + str(score_kevin))
    elif score_stuart > score_kevin:
        print("Stuart " + str(score_stuart))
    else:
        print("Draw")
    '''


if __name__ == '__main__':
    s = input()
    minion_game(s)
