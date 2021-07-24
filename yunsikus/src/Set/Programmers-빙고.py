def solution(board, nums):
    answer = 0
    N = len(board)
    set_nums = set(nums)

    col_sum = [0 for _ in range(N)]
    row_sum = [0 for _ in range(N)]
    diag_sum1 = 0
    diag_sum2 = 0

    for row in range(len(board)):
        for col in range(len(board)):
            if board[row][col] in set_nums:
                col_sum[col] += 1
                row_sum[row] += 1

            if (row == col) and board[row][col] in set_nums:
                diag_sum1 += 1

            if (row + col == N-1) and board[row][col] in set_nums:
                diag_sum2 += 1

    answer += len([x for x in col_sum if x == N])
    answer += len([x for x in row_sum if x == N])
    answer += diag_sum1 == N
    answer += diag_sum2 == N

    return answer
