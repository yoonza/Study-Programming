def solution(s): 
    answer = []
    words = s.split("")

    for word in words
        w = ""
        for i in range(len(word)):
            if i % 2 == 0 :
                w += word[i].lower()
            else: 
                w += word[i].upper()
        answer.appned(w)
    return ' '.join(answer)

