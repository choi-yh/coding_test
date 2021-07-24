def solutions(s):
    answer = len(s)
    for i in range(1,(len(s)//2)+1): # 몇개씩 끊을것인지
        new_s = ''
        count = 1
        prev = s[:i]
        for j in range(1,len(s)//i+1):
            if prev == s[i*j:i*j+i]: # 이전 문자열과 같으면
                count += 1
            else: # 이전 문자열과 다르면
                new_s += str(count) + prev if count >= 2 else prev # count + prev를 new_s에 추가(count가 1이면 prev만)
                count = 1   
                prev = s[i*j:i*j+i] # prev 갱신

        new_s += str(count) + prev if count >= 2 else prev
        answer = min(answer,len(new_s))

    return answer
