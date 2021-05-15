# 야구게임

# import random
#
# answer = random.sample(range(1, 9), 3)
# print(answer)
# while True:
#     s_num = 0
#     b_num = 0
#     t_num = 0
#
#     a, b, c = input('세자리 숫자를 입력하세요 : ').split()
#     a = int(a)
#     b = int(b)
#     c = int(c)
#     my = [a, b, c]
#
#     for i, answer_num in enumerate(answer):
#         for j, my_num in enumerate(my):
#             if answer_num == my_num and i == j:
#                 s_num += 1
#             elif answer_num == my_num and i != j:
#                 b_num += 1
#     print('스트라이크 : {}, 볼 : {}'.format(s_num, b_num))
#     if s_num == 3:
#         print('{}스트라이크 게임종료'.format(s_num))
#         break

# 빙고게임
# 1. 빙고 판 만들기
import random
row = 5
cal = 5

show_list = [[0 for i in range(row)] for j in range(cal)]
my_list = []
print(show_list)
for i in range(row):
    for j in range(cal):
        while True:
            ran_num = random.randint(1, 50)
            if ran_num not in my_list:
                show_list[i][j] = ran_num
                my_list.append(ran_num)
                break
print(show_list)

# 입력 받은 숫자 중 같은 것이 있으면 0으로 바꾸고 3 빙고 시 종료

while True:
    bingo = 0
    answer = int(input('1 ~ 50 중 숫자 하나를 입력하세요 : '))
    for i in range(row):
        for j in range(cal):
            if answer == my_list[i][j]:
                my_list[i][j] = 0
    c1 = 0
    c2 = 0
    for i in range(row):
        sum_x = 0
        sum_y = 0
        for j in range(cal):
            sum_x += my_list[i][j]
            sum_y += my_list[j][i]

        if sum_x == 0:
            bingo += 1
        if sum_y == 0:
            bingo += 1
        c1 += my_list[i][i]
        c2 += my_list[row - i - 1][i]
    if c1 == 0:
        bingo += 1
    if c2 == 0:
        bingo += 1
    print(my_list)
    print(bingo)

    if bingo > 2:
        print('빙~고')
        break

