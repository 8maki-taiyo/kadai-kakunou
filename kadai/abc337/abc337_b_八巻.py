# B の次に A が C の次に A or B が来るとダメそう

def hantei():
    S = input()
    for index in range(len(S)-1):
        if S[index] == "B":
            if S[index+1] == "A":
                return "No"
        elif S[index] == "C":
            if S[index+1] == "A" or S[index+1] == "B":
                return "No"
    return "Yes"

print(hantei())