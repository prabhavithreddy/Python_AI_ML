def get_permutations1(word):
    l = []
    for i in range(len(word)):
        for j in range(len(word)):
            for k in range(len(word)):
                if i != j and j != k and i != k:
                    l.append(word[i]+word[j]+word[k])
    return l

print(get_permutations1('ABC'))


