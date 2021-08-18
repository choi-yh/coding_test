def solution(genres, plays):
    answer = []
    zipped = [[x,y,z] for x, y, z in zip(genres, plays, range(len(plays)))]
    
    genre_set = set(genres) # 모든 장르 추출
    genre_count = {x:0 for x in genre_set} # genre와 플레이 횟수를 담을 dictionary 생성

    for arr in zipped: # 장르별 플레이 횟수 합산
        genre_count[arr[0]] += arr[1]

    genre_sorted = sorted(list(genre_count.items()), key = lambda x: -x[1]) # 플레이 횟수에 따라 장르 정렬
    
    for genre in genre_sorted: # 플레이 횟수가 많은 장르부터
        songs = [x for x in zipped if x[0] == genre[0]]
        songs.sort(key = lambda x : (-x[1],x[2])) # 플레이 횟수는 내림차순, 인덱스는 오름차순에 따라 정렬
        if len(songs) >= 2: # 장르에 음악이 2개 이상인 경우
            answer.append(songs[0][2])
            answer.append(songs[1][2])
        elif len(songs) == 1: # 장르에 음악이 하나인 경우
            answer.append(songs[0][2])
        
    return answer