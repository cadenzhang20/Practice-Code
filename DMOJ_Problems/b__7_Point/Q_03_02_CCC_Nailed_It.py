# https://dmoj.ca/problem/ccc17s3

amount_boards = int(input())
all_boards = list(map(int, input().split()))

board_count = {}

for b in all_boards:
    if b in board_count:
        board_count[b] += 1
    else:
        board_count[b] = 1

unique_boards = sorted(board_count.keys())

all_pairs = {}

for n1 in range(len(unique_boards) - 1):
    num_1 = unique_boards[n1]

    for num_2 in unique_boards[n1 + 1:]:
        pair = num_1 + num_2
        shared_pairs = min(board_count[num_1], board_count[num_2])
        if pair in all_pairs:
            all_pairs[pair] += shared_pairs
        else:
            all_pairs[pair] = shared_pairs

for num in unique_boards:
    pair = 2 * num
    if pair in all_pairs:
        all_pairs[pair] += board_count[num] // 2
    else:
        all_pairs[pair] = board_count[num] // 2

pairing_count = all_pairs.values()

fence_len = max(pairing_count)
amount_of_heights = 0

for num in pairing_count:
    if num == fence_len:
        amount_of_heights += 1

print(fence_len, amount_of_heights)
