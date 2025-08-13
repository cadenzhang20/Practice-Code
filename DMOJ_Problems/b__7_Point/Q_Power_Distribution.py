# https://dmoj.ca/problem/electricity

for _ in range(int(input())):
    home_count = int(input())
    on_list, off_list = [], []

    for _ in range(home_count):
        home_pos, home_state = [int(x) for x in input().split()]
        if home_state == 1: on_list.append(home_pos)
        else: off_list.append(home_pos)





# for _ in range(int(input())):
#     home_count = int(input())
#     on_list, off_list = [], []
#
#     for _ in range(home_count):
#         home_pos, home_state = [int(x) for x in input().split()]
#         if home_state == 1: on_list.append(home_pos)
#         else: off_list.append(home_pos)
#
#     begin_off, end_off = 0, len(off_list) - 1
#     while off_list[begin_off] < on_list[0]: begin_off += 1
#     while off_list[end_off] > on_list[-1]: end_off -= 1
#
#     cur_on = 0
#     wire = off_list[-1] - off_list[1]
#     cur_set = []
#     for h in range(begin_off, end_off):
#         if h < on_list[cur_on + 1]:
#             pass



