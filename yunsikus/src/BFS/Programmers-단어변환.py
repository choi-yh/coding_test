from collections import deque

def possible_words(begin, words):
    words_list = []
    for word in words:
        diff = 0
        for i in range(len(begin)):
            if begin[i] != word[i]:
                diff += 1
        if diff == 1:
            words_list.append(word)
    
    return words_list

def solution(begin, target, words):
    visited = []
    queue = deque()
    queue.append((begin,0))
    visited.append(begin)
    while queue:
        word, count = queue.popleft()
        if word == target:
            return count
        for next_word in possible_words(word, words):
            if next_word not in visited:
                queue.append((next_word, count+1))
                visited.append(next_word)
    return 0
