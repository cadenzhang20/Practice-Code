# https://dmoj.ca/problem/ccc12s3
# Not completed

count_reading = int(input())

min_first, max_first = 0, 0
min_sec, max_sec = 0, 0

my_list = [1, 2, 2, 3, 4, 4, 4, 5, 6]
most_num = my_list[0]
most_count = 1

for c in range(1, len(my_list)):
    if my_list[c] == most_num:
        most_count += 1
    else:
        most_count -= 1

    if most_count == 0:
        most_num = my_list[c]
        most_count += 1

print(most_num)

# count_reading = int(input())
# reading_list = [[x + 1, 0] for x in range(-1, 1000)]
#
# for _ in range(count_reading):
#     reading_list[int(input())][1] += 1
#
# def access(a): return a[1]
#
# reading_list.sort(key=access, reverse=True)
#
# first_common_count = reading_list[0][1]
# second_common_count = -1
#
# first_common_list, second_common_list = [], []
#
# c = 0
# while c < len(reading_list):
#     if reading_list[c][1] != first_common_count:
#         second_common_count = reading_list[c][1]
#         break
#     first_common_list.append(reading_list[c][0])
#     c += 1
#
# if second_common_count > 0:
#     while c < len(reading_list):
#         if reading_list[c][1] != second_common_count:
#             break
#         second_common_list.append(reading_list[c][0])
#         c += 1
#
# first_min, first_max = min(first_common_list), max(first_common_list)
#
# if not second_common_list:
#     print(first_max - first_min)
# else:
#     second_min, second_max = min(second_common_list), max(second_common_list)
#     possible = [abs(first_max - second_min), abs(second_max - first_min)]
#     print(max(possible))
