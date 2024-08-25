N = int(input())
S = input()

d = {}
s = ""
last_word = ""
for word in S:
    if word == last_word:
        s = s+word
        lest_word = word

    elif word != last_word:
        if len(s) != 0:
            if s[0] in d.keys():
                d[s[0]] = max([d[s[0]], len(s)])
            else:
                d[s[0]] = len(s)
        s = word
        last_word = word

    if s[0] in d.keys():
        d[s[0]] = max([d[s[0]], len(s)])
    else:
        d[s[0]] = len(s)
    

print(sum(d.values()))
