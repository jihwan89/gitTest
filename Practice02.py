# 빙고게임

# 1,2. 사용자에게 입력받은 값으로 가로세로 빙고판 만들기, 랜덤 숫자 체우기
# import random
# r_num, c_num = input("가로, 세로의 값을 입력하세요 : ").split()
# b_num = int(input("빙고판의 숫자범위를 입력하세요 : "))
# row = int(r_num)
# col = int(c_num)
#
# com_list = [0 for i in range(row) for j in range(col)]
# num_list = []
# for i in range(row):
#     for j in range(col):
#         while True:
#             random_num = random.randint(1, b_num)
#             if random_num not in num_list:
#                 com_list[i][j] = random_num
#                 num_list.append(random_num)
#                 break


import random
r_num, c_num = input("가로, 세로의 값을 입력하세요 : ").split()
b_num = int(input("빙고판의 숫자범위를 입력하세요 : "))
row = int(r_num)
col = int(c_num)

com_list = [[0 for i in range(row)] for j in range(col)]
num_list = []
for i in range(row):
    for j in range(col):
        while True:
            random_num = random.randint(1, b_num)
            if random_num not in num_list:
                com_list[i][j] = random_num
                num_list.append(random_num)
                break
print(com_list)

# 사용자에게 숫자 입력받기
# 입력받은 숫자 중 같은 것이 있으면 0으로 바꾸기
# 가로 한줄 또는 세로 한줄이 다 0이되면 빙고 카운트 올리기
# 3줄 빙고시 빙고 외치고 프로그램 종료


while True:
    bingo = 0
    my_num = int(input("숫자를 입력하세요 : "))
    for i in range(row):
        for j in range(col):
            if my_num == com_list[i][j]:
                com_list[i][j] = 0
    row_ = 0
    cross_ = 0
    for i in range(row):
        sum_row = 0
        sum_cal = 0
        for j in range(col):
            sum_row += com_list[i][j]
            sum_cal += com_list[j][i]
        if sum_row == 0:
            bingo += 1
        if sum_cal == 0:
            bingo += 1
        row_ += com_list[i][i]
        cross_ += com_list[row - i - 1][i]

    if row_ == 0:
        bingo += 1
    if cross_ == 0:
        bingo += 1
    print(com_list)
    print(bingo)

    if bingo > 2:
        print("Bingo!")
        break




