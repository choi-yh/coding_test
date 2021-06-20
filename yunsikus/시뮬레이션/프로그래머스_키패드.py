def dist(a,b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])

def solution(numbers, hand):
    answer = []
    curr_left = [0,3]
    curr_right = [2,3]

    for number in numbers:
        if number == 0:
            number = 11

        x_cord = (number-1) % 3
        y_cord = (number-1) // 3

        if number in [1,4,7]:
            # 왼쪽 엄지 좌표를 갱신
            curr_left = [x_cord, y_cord]
            answer += 'L'

        elif number in [3,6,9]:
            # 오른쪽 엄지 좌표를 갱신
            curr_right = [x_cord, y_cord]
            answer += 'R'

        else:
            distance_l = dist(curr_left, [x_cord, y_cord])
            distance_r = dist(curr_right, [x_cord, y_cord])

            if distance_l == distance_r:
                if hand == 'right':
                    answer += 'R'
                    curr_right = [x_cord, y_cord]
                else:
                    answer += 'L'
                    curr_left = [x_cord, y_cord]
            else:
                if distance_l < distance_r:
                    answer += 'L'
                    curr_left = [x_cord, y_cord]
                else:
                    answer += 'R'
                    curr_right = [x_cord, y_cord]
    return ''.join(answer)
